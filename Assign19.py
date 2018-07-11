#question 1,2
from tkinter import *
def display():
    w = Label(root, text = "you pressed button")
    w.pack()
    
root=Tk()
root.geometry("300x300")
root.title("introduction")
root.configure(background="grey")
hwL=Label(root,text="hello world!",font="times 26 bold underline")
hwL.pack()
clickL=Button(root,text="press here",font="none 20",command=display)
clickL.pack()
exitB=Button(root,text="exit",font="none 35",command=root.destroy)
exitB.pack(side=BOTTOM)
root.mainloop()

#question3
from tkinter import *
def change_text():
    labL.configure(text="text changed")
root=Tk()
root.title("frame")
root.geometry("300x300")
root.configure(background="grey")
frame_1=Frame(root,bg="red")
frame_1.pack(fill=X)
labL=Label(frame_1)
labL.configure(text="this is label",font="none 25")
labL.pack()
exitB=Button(root,text="exit",command=root.destroy,font="none 25")
chaL=Button(root,text="press here",command=change_text,font="none 20")
exitB.pack(side=BOTTOM)
chaL.pack()
root.mainloop()



#question 4
from tkinter import *
root=Tk()
root.title("copy")
root.geometry("300x300")
userL=Label(root,text="enter something ")
userL.pack()
userE=Entry(root)
userE.pack()
def display():
    r=Tk()
    r.title("next")
    hwL=Label(r,text=userE.get(),font="none 25")
    hwL.pack()
    exi=Button(r,text="exit",command=r.destroy)
    exi.pack()
    r.mainloop()
checkB=Button(root,text="click",font="none 25",command=display)
checkB.pack()
exitB=Button(root,text="exit",font="none 25",command=root.destroy)
exitB.pack()
root.mainloop()
