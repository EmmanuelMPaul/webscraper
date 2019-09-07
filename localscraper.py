import os

print('************************************************************')
print('*****************  Welcome to EC254 local scraper  ***********')
print('************************************************************')


def scrape():
    check = True
    try:
        # initialize varibles
        source = input('\tEnter file Name(e.g courses.txt): ')
        print('>>>scraping...')
        tags = open(source.strip(), "r", newline="")

        # set shell file
        localshellfile = "localcoursesdownloader.sh"
        f = open(localshellfile, "w+", newline="")
        f.write("#!/bin/bash \r\n")

        # prepare shell file
        for tag in tags:
            if os.path.isdir(tag):
                print(tag + ' course already exists!')
            else:
                cmd = "php codecourse download:course " + tag
                f.write(cmd)
                f.write("echo\r\necho -n '************************************************************'\r\n")
                f.write("echo\r\necho 'processing.... next course'\r\nsleep 5s\r\necho\r\n")

        f.write("echo -n press Enter or cmd to exit \r\n")
        f.write("read terminate")
        f.close()

    except FileNotFoundError:
        check = False
        print('Sorry! file "' + source + '" does not exist')

    if check:
        print('************************************************************')
        print("* DONE: " + localshellfile + " shell files generated")
        print('************************************************************')
        print('>>>downloading...')
        os.system(localshellfile)


while True:
    scrape()
    runAgain = input('Enter (yes|YES) to continue or press Enter or cmd to exit: ')
    if runAgain.lower() == "yes":
        print('*********************   New Run      ***********************')
    else:
        break
