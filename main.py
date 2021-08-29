import io
import os
import threading
import time
import tkinter.ttk
import tkinter.messagebox
import tkinter as tk
from pytube import YouTube
from pytube.cli import on_progress
from PIL import Image, ImageTk
from urllib.request import urlopen

def resize(w_box, h_box, pil_image):
  w, h = pil_image.size
  f1 = 1.0*w_box/w
  f2 = 1.0*h_box/h
  factor = min([f1, f2])
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.ANTIALIAS)

""" GUI """
yt = None
photo = None

def search():
    global yt
    url = set_URL.get()
    if not 'youtu' in url:
        tkinter.messagebox.showwarning(title='Error', message='不是YOUTUBE連結')
    yt = YouTube(url, on_progress_callback=on_progress)
    var.set(yt.title)

    image_bytes = urlopen(yt.thumbnail_url).read()
    data_stream = io.BytesIO(image_bytes)
    image = Image.open(data_stream)

    image = resize(600, 600, image)
    image = ImageTk.PhotoImage(image)

    label_img.configure(image=image)
    label_img.image = image
    window.update_idletasks()

    submit_bt.place(x=700, y=450)
    close_bt.place(x=900, y=450)
    progressbarOne.place(x=700, y=400)
    r1.place(x=700, y=250)
    r2.place(x=900, y=250)

window = tk.Tk()
var = tk.StringVar()
choice = tk.StringVar()
choice.set('video')

window.title('Youtube下載器')
#bg = '#DDA0DD'
window.geometry('1100x600')

canvas = tk.Canvas(window, width=1100,height=600,bg='Thistle', highlightthickness=0)
canvas.pack()

set_URL = tk.Entry(window, font=('Arial', 20), width=58)
set_URL.place(x = 50, y = 30)
#t = tk.Text(window, height=1, font=('Arial', 14))
#t.place(x = 50, y = 50)
search_bt = tk.Button(window, text='搜尋', font=('微軟正黑體', 15), width=8, height=1, command=search)
search_bt.place(x = 950, y = 20)

l = tk.Label(window, textvariable=var, font=('微軟正黑體', 15), height=2, bg='Thistle')
l.place(x = 50, y = 70)

label_img = tk.Label(window, image=photo, bg='Thistle')
label_img.place(x = 50, y = 120)

def submit():
    global yt
    if choice.get() == 'video':
        #print(choice.get())
        try:
            stream = yt.streams.get_by_itag(22)
            stream.download()
        except:
            try:
                stream = yt.streams.get_by_itag(18)
                stream.download()
            except:
                stream = yt.streams.filter(progressive=True).first()
                stream.download()

        tkinter.messagebox.showinfo(title='通知', message='下載完成')
    else:
        #print(choice.get())
        try:
            stream = yt.streams.get_by_itag(140)
            stream.download(filename_prefix='music')
        except:
            stream = yt.streams.get_by_itag(139)
            stream.download(filename_prefix='music')

        tkinter.messagebox.showinfo(title='通知', message='下載完成')

def close():
    window.destroy()

submit_bt = tk.Button(window, text='下載', font=('微軟正黑體', 18), width=10, height=1, command = submit)
close_bt = tk.Button(window, text='關閉', font=('微軟正黑體', 18), width=10, height=1, command = close)

r1 = tk.Radiobutton(window, text='影片', font=('微軟正黑體', 18), variable=choice, value='video', bg='Thistle')
r2 = tk.Radiobutton(window, text='音樂', font=('微軟正黑體', 18), variable=choice, value='music', bg='Thistle')

progressbarOne = tkinter.ttk.Progressbar(window, length=350)


window.mainloop()