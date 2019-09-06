import os
import re
import requests
from bs4 import BeautifulSoup

print('************************************************************')
print('*******************  Welcome to EC254 scraper  *************')
print('************************************************************')
def scrape():
    # loop all pages
    shellfilename = "courses.sh"
    coursefilename = "courses.txt"
    c = open(coursefilename, "w+", newline="")
    f = open(shellfilename, "w+", newline="")
    f.write("#!/bin/bash \r\n")
    startPage = input('\tEnter START page number: ')
    endPage = input('\tEnter END page number: ')
    # loop all pages
    index = 1;
    for page in range(int(startPage), int(endPage) + 1, 1):
        response = requests.get('https://codecourse.com/library/all?free=false&page=' + str(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        courses = soup.find_all('a', href=True)
        # course
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
    print("*\tDONE: " + shellfilename + " and " + coursefilename + "files generated")
    print('************************************************************')
    os.system("courses.sh")
while 1:
    scrape()
    runAgain = input('Enter (yes|YES) to continue or press Enter or cmd to exit: ')
    if runAgain.lower() == "yes":
        print('*********************   New Run      ***********************')
    else:
        break
