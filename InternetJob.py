from xmlJob import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer


##global
conn = None
regKey = "WNJ2ZX96FAX7OEYLSQFRI2VR1HK"

# 네이버 OpenAPI 접속 정보 information
server = "openapi.work.go.kr"

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

def userURIBuilder(server,**user):
    str = "http://" + server + "/opi/opi/opia/jobSrch.do" + "?"
    for key in user.keys():
        str += (key + "=" + user[key] + "&")
    return str

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

def extractData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print (strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("jobSum")  # return list type
    for item in itemElements:
        strTitle = item.find("jobSmclNm")
        summary = item.find("jobSum")
    #    way = item.find("way")
    #   jobVideo = item.find("jobSum")
    #    print(strTitle)

        if len(strTitle.text) > 0 :
            return {"Title":strTitle.text,"summary":summary.text}

def getData(job):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
        #authKey=WNJ2ZX96FAX7OEYLSQFRI2VR1HK&returnType=XML&target=JOBDTL&jobGb=1&jobCd=20120&dtlGb=1
    uri = userURIBuilder(server, authKey=regKey, returnType="XML", target="JOBDTL", jobGb="1", jobCd=str(job), dtlGb="1")
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        return extractData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True