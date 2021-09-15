import tkinter as tk
from tkinter import ttk
import os
from pytube import YouTube
from tkinter import messagebox as m_box
import subprocess
import threading
 
 
def Download():
    got_link = link.get()
    got_path = path.get()
    try:
        yt = YouTube(str(got_link))
    except:
        m_box.showerror("Error", "การเชื่อมต่อมีปัญหา")
    else:
        vid = yt.streams.get_highest_resolution()
        destination = str(got_path)
        vid.download(destination)
        os.startfile(got_path)
        return m_box.showinfo('Successfully Downloaded.', f"Your YouTube Vidoe Downloaded Successfully at {got_path}/{yt.title}")
 
 
threads = []
 
 
def startThredProcess():
    myNewThread = threading.Thread(target=Download)
    threads.append(myNewThread)
    myNewThread.start()
 
#set window
win = tk.Tk()
win.geometry("390x160")
win.title("YouTube Download")
win.minsize(390, 160)
win.maxsize(390, 160)
 
 
#set grid
frame = ttk.LabelFrame(win)
frame.grid(row=0, column=1, padx=10, pady=2)
 
 
 
#add label
get_info = ttk.Label(frame, text="Enter YouTube Link : ")
get_info.grid(row=0, column=0, sticky=tk.W)
 
#get var
link = tk.StringVar()
 
#add input
yt_link = ttk.Entry(frame, width=60, textvariable=link)
yt_link.grid(row=1, columnspan=3, padx=0, pady=3)
yt_link.focus()
 
get_info = ttk.Label(frame, text="Enter To Save Path : ")
get_info.grid(row=3, column=0, sticky=tk.W)
 
#get var path
path = tk.StringVar()
 
#add input
download_path = ttk.Entry(frame, width=60, textvariable=path)
download_path.grid(row=4, columnspan=3, padx=0, pady=3)
 
#add button
btd = ttk.Button(frame, text="Download ตอนนี้",
                  width=15, command=startThredProcess)
btd.grid(row=7, columnspan=3, padx=13, pady=7)
 
win.mainloop()