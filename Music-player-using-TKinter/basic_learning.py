from tkinter import *


def button_click():
    print('Button clicked')
    
root = Tk()
root.geometry("720x480")   #width x height

title = Label(root, text='First Window', fg="#DA3636", font=('', 32))
title.pack()

button_1 = Button(root, text='Click', command=button_click)
button_1.pack(side=TOP) # pack sets the button in a convenient position

root.mainloop()