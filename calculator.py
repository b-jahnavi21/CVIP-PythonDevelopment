from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                value="Error"
        
        scvalue.set(value)
        screen.update()
    
    elif text=="C":
        scvalue.set("")
        screen.update()
    
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("250x450")
root.title("Calculator Application")
img=PhotoImage(file='icon.png')
root.iconphoto(False,img)

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 25 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg='grey')
b=Button(f,text="9",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="8",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="7",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

f.pack()


f=Frame(root,bg='grey')
b=Button(f,text="6",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="5",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="4",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

f.pack()


f=Frame(root,bg='grey')
b=Button(f,text="3",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="2",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="1",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

f.pack()


f=Frame(root,bg='grey')
b=Button(f,text="0",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="- ",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="* ",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

f.pack()


f=Frame(root,bg='grey')
b=Button(f,text="/",font="lucida 14 bold",padx=17,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="%",font="lucida 14 bold",padx=11,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="=",font="lucida 14 bold",padx=15,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

f.pack()


f=Frame(root,bg='grey')
b=Button(f,text="C",font="lucida 14 bold",padx=13,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text=".",font="lucida 14 bold",padx=18,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

b=Button(f,text="00",font="lucida 14 bold",padx=10,pady=5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=5,pady=5)

f.pack()

root.configure(background='grey')

width=root.winfo_screenwidth()
height=root.winfo_screenheight()


root.mainloop()
