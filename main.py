import tkinter
from tkinter import *


window = tkinter.Tk()
window.title('GUI')
window.geometry('700x200')

label = Label(window, text = "Hello World",font = ('Arial Bold', 50 ))
label.grid(column = 0, row = 0)

def clicked():
    res = "Welcom to " + entry_list[0].get()
    label.configure(text = res)

bt = Button(window, text = "Enter",fg = "red", bg = "white",command = clicked)
bt.grid(column = 0, row = 1)

entry_list = []
entry_list.append(Entry(window, width = 10))
entry_list[0].grid(column = 1, row = 1)

window.mainloop()
