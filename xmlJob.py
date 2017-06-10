from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

xmlFD = -1
JobsDoc = None


def PrintJobList(tags):
    global JobsDoc
    if not checkDocument():
        return None

    joblist = JobsDoc.childNodes
    job = joblist[0].childNodes
    for item in job:
        if item.nodeName == "jobList":
            subitems = item.childNodes
            for atom in subitems:
                if atom.nodeName in tags:
                    if atom.nodeName == "jobCd":
                        print("직업 코드:" ,atom.firstChild.nodeValue)
                    else:
                        print(atom.firstChild.nodeValue)
                        print("\n")


def SearchJobTitle(keyword):
    global JobsDoc
    retlist = []
    if not checkDocument():
        return None

    try:
        tree = ElementTree.fromstring(str(JobsDoc.toxml()))
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # get Book Element
    jobElements = tree.getiterator("jobList")  # return list type
    for item in jobElements:
        strTitle = item.find("jobNm")
        strCd = item.find("jobCd")
        if (strTitle.text.find(keyword) >= 0):
            retlist.append(strTitle.text)
            retlist.append(strCd.text)

    for element in retlist:
        print(element)

def MakeHtmlDoc(jobList):
    from xml.dom.minidom import getDOMImplementation
    # get Dom Implementation
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for jobitem in jobList.items():
        # create bold element
        b = newdoc.createElement('b')
        # create text node
        ibsnText = newdoc.createTextNode(jobitem[0])
        b.appendChild(ibsnText)

        body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode(jobitem[1])
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  # line end

    # append Body
    top_element.appendChild(body)

    return newdoc.toxml()

def checkDocument():
    global JobsDoc
    if JobsDoc == None:
        return False
    return True


def JobsFree():
    if checkDocument():
        JobsDoc.unlink()

