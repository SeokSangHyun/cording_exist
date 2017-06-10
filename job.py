from InternetJob import *
from xmlJob import *
import urllib.request
from tkinter import font
from tkinter import *

##########
#global
loopFlag = 1
window = Tk()
window.geometry("600x650+750+200")


def InitTopText():
    topFont = font.Font(window, size=30, weight = 'bold', family = "Arial" )
    MainText = Label(window, font=topFont, text="[당신의 직업을 찾아드립니다!]")
    MainText.pack()
    MainText.place(x=20)

def InitPayListBox(): #연봉별 검색 박스
    global SearchListBox

    LeftFont = font.Font(window, size=20, weight = 'bold', family = "Arial" )
    LeftText = Label(window, font=LeftFont, text="연봉별 검색")
    LeftText.pack()
    LeftText.place(x=10, y= 60)

    ## 스크롤바
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=450, y=50)

    ##검색박스
    TempFont = font.Font(window, size=20, weight='bold', family='Arial')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none', width=15, height=1, borderwidth=12, relief='ridge',yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "3천만 미만")
    SearchListBox.insert(2, "3천만~4천만")
    SearchListBox.insert(3, "4천만~5천만")
    SearchListBox.insert(4, "5천만이상")
    SearchListBox.pack()
    SearchListBox.place(x=200, y=50)

    ListBoxScrollbar.config(command=SearchListBox.yview)

    ###검색 버튼
    searchFont = font.Font(window, size = 12, weight = 'bold', family = 'Arial')
    SearchButton = Button(window, font = searchFont, text = '검색', command = SearchPayButtonAction)
    SearchButton.pack()
    SearchButton.place(x = 500, y = 60)
    SearchButton["bg"] = "yellow"

def SearchPayButtonAction():
    global SearchListBox
    global ret

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        ret = getpayData(1)
    elif iSearchIndex == 1:
        ret = getpayData(2)
    elif iSearchIndex == 2:
        ret = getpayData(3)
    elif iSearchIndex == 3:
        ret = getpayData(4)

    #연봉별 검색 출력
    num = 1
    for i in ret.items():
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, num)
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "직업명: ")
        RenderText.insert(INSERT, i[0])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "직업코드: ")
        RenderText.insert(INSERT, i[1])
        RenderText.insert(INSERT, "\n\n")
        num+=1
    RenderText.configure(state='disabled')

def InitCateListBox():
    global InputCateLabel

    LeftFont = font.Font(window, size=20, weight='bold', family="Arial")
    LeftText = Label(window, font=LeftFont, text="카테고리 검색")
    LeftText.pack()
    LeftText.place(x=10, y=130)

    ##검색박스
    TempFont = font.Font(window, size=20, weight='bold', family='Arial')
    InputCateLabel = Entry(window, font = TempFont, width = 15, borderwidth = 12, relief = 'ridge')
    InputCateLabel.pack()
    InputCateLabel.place(x=200, y=120)

    ###검색 버튼
    searchFont = font.Font(window, size=12, weight='bold', family='Arial')
    SearchButton = Button(window, font=searchFont, text='검색', command=SearchCateButtonAction)
    SearchButton.pack()
    SearchButton.place(x=500, y=130)
    SearchButton["bg"] = "yellow"


def SearchCateButtonAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    EncName = urllib.parse.quote(InputCateLabel.get())
    buf = getList(EncName)
    num = 1
    for i in buf:
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, num)
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "직업분류 코드: ")
        RenderText.insert(INSERT, buf[i][1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "직업명: ")
        RenderText.insert(INSERT, i)
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "직업코드: ")
        RenderText.insert(INSERT, buf[i][0])
        RenderText.insert(INSERT, "\n\n")
        num += 1
    RenderText.configure(state='disabled')

def InitCodeBox():
    global InputCodeLabel

    LeftFont = font.Font(window, size=12, weight='bold', family="Arial")
    LeftText = Label(window, font=LeftFont, text="직업코드(세부정보) 검색")
    LeftText.pack()
    LeftText.place(x=10, y=215)

    ##검색박스
    TempFont = font.Font(window, size=20, weight='bold', family='Arial')
    InputCodeLabel = Entry(window, font=TempFont, width=15, borderwidth=12, relief='ridge')
    InputCodeLabel.pack()
    InputCodeLabel.place(x=200, y=200)

    ###검색 버튼
    searchFont = font.Font(window, size=12, weight='bold', family='Arial')
    SearchButton = Button(window, font=searchFont, text='검색', command=CodeButtonAction)
    SearchButton.pack()
    SearchButton.place(x=500, y=215)
    SearchButton["bg"] = "yellow"

def CodeButtonAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    buf = getData(InputCodeLabel.get())

    for i in buf:
        RenderText.insert(INSERT, "직업명: ")
        RenderText.insert(INSERT, i)
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "설명: ")
        RenderText.insert(INSERT, buf[i][0])
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "되는길: ")
        RenderText.insert(INSERT, buf[i][1])
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "연봉: ")
        RenderText.insert(INSERT, buf[i][2])
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "직업만족도: ")
        RenderText.insert(INSERT, buf[i][3])
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "직업전망: ")
        RenderText.insert(INSERT, buf[i][4])
        RenderText.insert(INSERT, "\n\n")

    RenderText.configure(state='disabled')

def InitRenderText():
    global RenderText
    global InputCodLabel

    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y = 200)

    TempFont = font.Font(window, size=10, family='Arial')
    RenderText = Text(window, width=78, height=20, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place (x=10, y=280)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')


    #####
    # 메일보내기
    LeftFont = font.Font(window, size=12, weight='bold', family="Arial")
    LeftText = Label(window, font=LeftFont, text="직업코드입력")
    LeftText.pack()
    LeftText.place(x=30, y=590)

    TempFont = font.Font(window, size=15, weight='bold', family='Arial')
    InputCodLabel = Entry(window, font=TempFont, width=10, borderwidth=12, relief='ridge')
    InputCodLabel.pack()
    InputCodLabel.place(x=140, y=580)

    searchFont = font.Font(window, size=15, weight='bold', family='Arial')
    mailButton = Button(window, font=searchFont, text='메일 전송', command=SearchMailButtonAction)
    mailButton.pack()
    mailButton.place(x=300, y=585)
    mailButton["fg"] = "White"
    mailButton["bg"] = "Blue"

def SearchMailButtonAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    code = InputCodLabel.get()
    sendMain(code)
    RenderText.insert(INSERT, "메일 전송 성공!")
    RenderText.configure(state='disabled')

######################
#tkinter

InitTopText()
InitPayListBox()
InitCateListBox()
InitCodeBox()
InitRenderText()

window.mainloop()