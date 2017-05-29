loopFlag = 1
from InternetJob import *
import urllib.request

def launcherFunction(menu):
    if menu == 'l':
        LoadXMLFromFile()
    elif menu == 'b':
        EncName = input("검색 할 직업군을 적어주세요. : ")
        EncName = urllib.parse.quote(EncName)
        buf = PrintJobList(EncName)
        for x in buf:
            print(buf[x][1], x, buf[x][0])
        print("... 추가로 검색을 하시겠습니까? ...(y/n)")
        if(input() == 'n'):
            pass
        else:
            name = input("직업명을 입력 하세요. : ")
            for x in buf:
                if x == name:
                    temp = {x: (buf[x][0], buf[x][1])}
                    buf = NameSearch(temp)
                    print(buf)

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
    print("Print All:       b")
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