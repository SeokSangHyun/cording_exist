loopFlag = 1
from InternetJob import *

def launcherFunction(menu):
    if menu == 'l':
        LoadXMLFromFile()
    elif menu == 'b':
        PrintList(["title", ])
    elif menu == 'a':
        str = input("직업번호를 입력하시오.")
        ret = getData(str)
        print(ret)
    elif menu == 'q':
        Run()


def printMenu():
    print("₩nWelcome! Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:        l")
    print("Load API:        a")
    print("Print All:       p")
    print("Quit program:    q")
    print("========Menu==========")

def Run():
    global loopFlag
    loopFlag = 0
    Free()

##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")