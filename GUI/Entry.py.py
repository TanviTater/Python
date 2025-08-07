from tkinter import *
root = Tk()
e = Entry(root,width = 50,bg = "light blue",fg = "black",font = ("Arial", 12),borderwidth=5)
e.pack()
e.insert(0,"Enter Your Name")
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root,text =hello)
    myLabel.pack()
myButton = Button(root,text = "Enter Your name",command = myClick)
myButton.pack()
root.mainloop()