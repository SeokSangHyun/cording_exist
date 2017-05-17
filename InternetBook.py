from xmlBook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer


##global
conn = None
regKey = "65d131ea113137d9e82c141f30421353"

# 네이버 OpenAPI 접속 정보 information
server = "apis.daum.net"

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True