from tkinter import *
root = Tk()
myLabel = Label(root , text = "Hello World")
myLabel2 = Label(root, text = "Welcome to GUI Programming")
myLabel.grid(row =0,column = 0)
myLabel2.grid(row =1,column =2)
root.mainloop()