#coding=utf-8

import tkinter
import os
from tkinter import *
from tkinter.simpledialog import *



def btn_click():
    global entryVarUsername
    global entryVarPassword
    global gUserName
    cmd = "user.exe \"%s\" \"%s\"" % (entryVarUsername.get(),entryVarPassword.get())
    ret = os.system(cmd)
    # print(ret)
    global root
    if ret == 0:
        dlg = SimpleDialog(root,text="Can not find user name",buttons=["OK"])
        dlg.go()
        pass
    elif ret == 1:
        dlg = SimpleDialog(root,text="Password Wrong",buttons=["OK"])
        dlg.go()
        pass
    elif ret == 2:
        gUserName = entryVarUsername.get()
        root.destroy()
    else:
        dlg = SimpleDialog(root,text="Error",buttons=["OK"])
        dlg.go()

def main():
    global gUserName,root
    gUserName = ''
    root = Tk()
    root.title("Log In")
    windowWidth = 300
    windowHeight = 250
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight,  (ws / 2) - (windowWidth / 2), (hs / 2) - (windowHeight / 2)))
    fm = Frame(root)
    Label(fm).grid(row=0,column=0)
    Label(fm,text="User Name:").grid(row=1,column=0,padx=20,pady=20)
    global entryVarUsername
    entryVarUsername = StringVar()
    Entry(fm,textvariable=entryVarUsername).grid(row=1,column=1)
    Label(fm,text="Password:").grid(row=2,column=0,padx=20,pady=20)
    global entryVarPassword
    entryVarPassword = StringVar()
    entry2 = Entry(fm,textvariable=entryVarPassword)
    entry2.grid(row=2,column=1)
    entry2['show'] = '*'
    Label(fm).grid(row=3,column=0)
    Button(fm,text="  LogIn  ",command=btn_click).grid(row=4,column=0,columnspan=2)
    fm.pack()
    root.mainloop()	

if __name__ == '__main__':
    main()

