import socket
import time
import threading
from tkinter import *

root=Tk()
root.geometry("300x500")
root.config(bg="white")

def startmessagethread():
    t=threading.Thread(target=recv)
    t.start()

def recv():
    listensocket=socket.socket()
    port=3050
    ip=socket.gethostname()
    print(ip)

    listensocket.bind()
    listensocket.listen(99)
    (clientsocket,address)=listensocket.accept()

    while 1:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            listbox.insert(0,"PERSON 1:"+sendermessage)

flag=0
def send():
    global flag
    s=socket.socket()
    if flag==0:
        #s=socket.socket()
        hostname="desktop"
        port=3050
        s.connect((hostname,port))
        msg=messagebox.get()
        listbox.insert(0,"You: "+msg)
        s.send(msg.encode())
        flag+=1
    else:
        msg=messagebox.get()
        listbox.insert(0,"You: "+msg)
        s.send(msg.encode())

    



def threadsendmessage():
    t=threading.Thread(target=send)
    t.start()






startchatimage=PhotoImage(file="start.png")
startimagebutton=Button(root,image=startchatimage,command=startmessagethread,borderwidth=0)
startimagebutton.place(x=90,y=10)

listbox=Listbox(root,height=20,width=43)
listbox.place(x=15,y=80)

messagebox=Entry(root,textvariable=StringVar(),font=("calibre",10,"normal"),border=2,width=32)
messagebox.place(x=10,y=444)

sendmessageimage=PhotoImage(file="send.png")
sendmessagebutton=Button(root,image=sendmessageimage,command=threadsendmessage,borderwidth=0)
sendmessagebutton.place(x=260,y=440)

root.mainloop()

