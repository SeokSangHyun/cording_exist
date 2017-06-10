from xmlJob import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
regKey = "WNJ2ZX96FAX7OEYLSQFRI2VR1HK"

# 워크넷 OpenAPI 접속 정보 information
server = "openapi.work.go.kr"

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"


def userURIBuilder(server,**user):
    str = "http://" + server + "/opi/opi/opia/jobSrch.do" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

def getData(job):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
        #&returnType=XML&target=JOBDTL&jobGb=1&jobCd=2&dtlGb=1
    uri = userURIBuilder(server, authKey=regKey, returnType="xml", target="JOBDTL", jobGb="1", jobCd=str(job), dtlGb="1")
    conn.request("GET", uri)

    req = conn.getresponse()
    return extractData(req.read())

def extractData(strXml):
    global conn
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    #print (strXml)
    # Book 엘리먼트를 가져옵니다.

    itemList = {}
    itemElements = tree.getiterator("jobSum")  # return list type
    for item in itemElements:
        strTitle = item.find("jobSmclNm")
        summary = item.find("jobSum")
        way = item.find("way")
        jobVideo = item.find("jobSum")
        sal = item.find("sal")
        jobSatis = item.find("jobSatis")
        jobProspect = item.find("jobProspect")

        itemList[strTitle.text] =(summary.text, way.text, sal.text, jobSatis.text, jobProspect.text)

    #    print(strTitle)
        conn.close()
        conn = None
        if len(strTitle.text) > 0 :
            #return {"직업 명:":strTitle.text, "설명:":summary.text, "되는길:":way.text, "연봉:":sal.text, "직업만족도:":jobSatis.text, "직업전망:":jobProspect.text}
            return itemList

def getpayData(num):
    global server, regKey, conn
    global uri2
    if conn == None:
        connectOpenAPIServer()
        uri2 = userURIBuilder(server, authKey=regKey, returnType="xml", target="JOBCD", srchType="c", avgSal = str(num))
    conn.request("GET", uri2)

    req = conn.getresponse()
    return extractData_pay(req.read())


def extractData_pay(strXml):
    global conn
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)

    payList={}
    itemElements = tree.getiterator("jobList")  # return list type

    for item in itemElements:
        strTitle = item.find("jobNm")
        code = item.find("jobCd")
        payList[strTitle.text] = code.text
    conn.close()
    conn = None
    if len(strTitle.text) > 0:
        return payList

def getList(category):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
        #authKey = WNJ2ZX96FAX7OEYLSQFRI2VR1HK & returnType = XML & target = JOBCD & srchType = K & keyword = % EA % B5 % 90 % EC % 82 % AC
        # 교사 = %EA%B5%90%EC%82%AC
    uri3 = userURIBuilder(server, authKey=regKey, returnType="XML", target="JOBCD", srchType="K", keyword=str(category))
    conn.request("GET", uri3)

    req = conn.getresponse()
    #print(req.status)
    if int(req.status) == 200:
        print("list downloading complete!")
        return ListData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def ListData(strXml):
    global conn
    from xml.etree import ElementTree

    tree = ElementTree.fromstring(strXml)
    #print(strXml)

    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("jobList")  # return list type
    temp = {}
    for item in itemElements:
        strcd = item.find("jobCd")
        strgb = item.find("jobGb")
        strNm = item.find("jobNm")
        #    print(strTitle)
        temp[strNm.text] = (strcd.text, strgb.text)
    conn.close()
    conn = None
    return temp


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True


def sendMain(keyword):
    global host, port
    html = ""
    title = "직업정보" #메일 제목
    senderAddr = "ychangmin94@gmail.com" #보내는 사람
    recipientAddr = "min940913@naver.com" #받는 사람
    msgtext = "mail" #메일 내용
    passwd = "charizard1!"
    msgtext = "y"
    if msgtext == 'y' :
        html = MakeHtmlDoc(getData(keyword))

    import mysmtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")