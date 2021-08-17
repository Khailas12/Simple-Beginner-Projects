from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')    # geometry() used to set the window’s width and height
root.resizable(0,0)
root.title("iNet")

Label(root, text= "YouTube Video downloader", font = 'arial 20 bold').pack()   #Label() widget use to display text that users can’t able to modify.

link = StringVar()  #StringVar is a class that provides helper functions for directly creating and accessing such variables in that interpreter.
# # Holds a string; the default value is an empty string ""

Label(root, text = "Paste The Link Here: ", font= 'arial 15 bold').place(x= 160, y=60)
link_enter = Entry(root, width= 70, textvariable= link, font= 'arial 12').place(x= 32, y = 90)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, Text= 'DOWNLOAD', font = 'arial 15').place(x= 180, y=210)

Button(root, text= 'DOWNLOAD', font= 'ariel 15 bold', bg= 'red', padx= 2, command= Downloader).place(x=180, y=150)

root.mainloop()




# https://bit.ly/3565YYD => go to this site for further quries




