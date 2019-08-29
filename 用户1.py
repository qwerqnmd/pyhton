import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("用户1")
win.geometry("400x450")

ck = None#用于储存客户端的信息


def getInfo():
    while True:
        data = ck.recv(1024)#用于接受服务其发送的信息
        text.insert(tkinter.INSERT, data.decode("utf-8"))#显示在信息框上


def connectServer():
    global ck
    ipStr = eip.get()
    portStr = eport.get()
    userStr = euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socked所准守ipv4或ipv6，和相关协议的
    client.connect((ipStr, int(portStr)))#连接ip和端口号！！！1:注意输入的端口号是str型而这里的要传入int型
    #2:bind()的参数是一个元组的形式
    client.send(userStr.encode("utf-8"))
    ck = client

    t = threading.Thread(target=getInfo)
    t.start()


def sendMail():
    friend = efriend.get()
    sendStr = esend.get()
    sendStr = friend + ":" + sendStr
    ck.send(sendStr.encode("utf-8"))


#下面是界面
labelUse = tkinter.Label(win, bd=10,text="userName").grid(row=0, column=0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win,bd=10, textvariable=euser).grid(row=0, column=1)

labelIp = tkinter.Label(win,bd=10, text="ip").grid(row=1, column=0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win, bd=10,textvariable=eip).grid(row=1, column=1)

labelPort = tkinter.Label(win,bd=10, text="port").grid(row=2, column=0)
eport = tkinter.Variable()

entryPort = tkinter.Entry(win, bd=10,textvariable=eport).grid(row=2, column=1)

button = tkinter.Button(win, bd=10,text="启动", command=connectServer).grid(row=3, column=0)
text = tkinter.Text(win,bd=10, height=5, width=30)


esend = tkinter.Variable()
labelesend = tkinter.Label(win,bd=10, text="发送的消息").grid(row=5, column=0)
entrySend = tkinter.Entry(win,bd=10, textvariable=esend).grid(row=5, column=1)

efriend = tkinter.Variable()
labelefriend= tkinter.Label(win, bd=10,text="发给谁").grid(row=6, column=0)
entryFriend = tkinter.Entry(win,bd=10, textvariable=efriend).grid(row=6, column=1)

button2 = tkinter.Button(win,bd=10, text="发送", command=sendMail).grid(row=7, column=0)

labeltext= tkinter.Label(win, bd=10,text="显示消息").grid(row=8, column=0)
text.grid(row=9, column=1)

win.mainloop()
