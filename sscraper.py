import os
import re
import requests
from bs4 import BeautifulSoup

print('************************************************************')
print('**************  Welcome to EC254 Snippet scraper  **********')
print('************************************************************')


def scrape():
    # set files
    shellfilename = "snippetdownloader.sh"
    snippetsfilename = "snippetlist.txt"
    c = open(snippetsfilename, "w+", newline="")
    f = open(shellfilename, "w+", newline="")
    f.write("#!/bin/bash \r\n")    
    # initialize varibles
    start = input('\tEnter START page number: ')
    end = input('\tEnter END page number: ')
    print('>>>scraping...')
    # loop all pages
    for page in range(int(start), int(end) + 1, 1):
        response = requests.get('https://codecourse.com/library/all?free=false&page='+str(page)+'&type=snippet')
        soup = BeautifulSoup(response.text, 'html.parser')
        courses = soup.find_all('a', href=True)

        # loop courses in a page
        ignore = ''
        for course in courses:
            link = course['href']
            # validate link
            if re.search(r"^/courses/", link):
                tag = link[9:len(link)]
                if ignore != tag:
                    cmd = "php codecourse download:course " + tag + "\r\n"
                    f.write(cmd)
                    c.write(tag + "\r\n")
                    f.write("echo\r\necho -n '************************************************************'\r\n")
                    f.write("echo\r\necho 'processing.... next course'\r\nsleep 5s\r\necho\r\n")
                ignore = tag

    f.write("echo -n press Enter or cmd to exit \r\n")
    f.write("read terminate")
    f.close()
    c.close()

    print('************************************************************')
    print("*\tDONE: " + shellfilename + " and " + snippetsfilename + "files generated")
    print('************************************************************')
    print('>>>downloading...')
    os.system(shellfilename)


while True:
    scrape()
    runAgain = input('Enter (yes|YES) to continue or press Enter or cmd to exit: ')

    if runAgain.lower() == "yes":
        print('*********************   New Run      ***********************')
    else:
        break
