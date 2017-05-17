loopFlag = 1
from InternetBook import *

def launcherFunction(menu):
    if menu == 'l':
        LoadXMLFromFile()
    elif menu == 'q':
        Run()


def printMenu():
    print("₩nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Quit program:   q")
    print("========Menu==========")

def Run():
    global loopFlag
    loopFlag = 0
    BooksFree()

##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")