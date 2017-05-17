from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

xmlFD = -1
BooksDoc = None

#### xml 관련 함수 구현
def LoadXMLFromFile():
    fileName = str(input ("please input file name to load :"))
    global xmlFD, BooksDoc
    try:
        xmlFD = open(fileName)
    except IOError:
        print ("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print ("loading fail!!!")
        else:
            print ("XML Document loading complete")
            BooksDoc = dom
            return dom
    return None


def BooksFree():
    if checkDocument():
        BooksDoc.unlink()

def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True