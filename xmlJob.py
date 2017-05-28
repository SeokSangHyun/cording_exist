from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

xmlFD = -1
JobsDoc = None

#### xml 관련 함수 구현
def LoadXMLFromFile():
    fileName = str(input ("please input file name to load :"))
    global xmlFD, JobsDoc
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
            JobsDoc = dom
            return dom
    return None

def Add(data):
    global JobsDoc
    if not checkDocument():
        return None

    # book 엘리먼트 생성
    newJob = JobsDoc.createElement('jobSum')
    newJob.setAttribute('jobSmclNm', data['jobSmclNm'])
    # Title 엘리먼트 생성
    titleEle = JobsDoc.createElement('jobSmclNm')
    # 텍스트 노드 생성
    titleNode = JobsDoc.createTextNode(data['jobSmclNm'])
    # 텍스트 노드를 Title 엘리먼트와 연결
    try:
        titleEle.appendChild(titleNode)
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        titleEle.appendChild(titleNode)



    # Title 엘리먼트를 Book 엘리먼트와 연결.
    try:
        Joblist.appendChild(titleEle)
        Joblist = JobsDoc.firstChild
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if Joblist != None:
            Joblist.appendChild(Joblist)

def PrintList(tags):
    global JobsDoc
    if not checkDocument():
        return None

    booklist = JobsDoc.childNodes
    book = booklist[0].childNodes
    for item in book:
        if item.nodeName == "book":
            subitems = item.childNodes
            for atom in subitems:
                if atom.nodeName in tags:
                    print("title=", atom.firstChild.nodeValue)



def Free():
    if checkDocument():
        Doc.unlink()

def checkDocument():
    global JobsDoc
    if JobsDoc == None:
        print("Error : Document is empty")
        return False
    return True