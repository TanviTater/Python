from tkinter import *
root =Tk()
def myClick():
    myLabel = Label(root, text = "You Clicked the button!")
    myLabel.pack()
myButton = Button(root,text = "Click Me!",padx = 50,pady =50,command=myClick,fg = "blue",bg="#000000")
myButton.pack()
root.mainloop()  