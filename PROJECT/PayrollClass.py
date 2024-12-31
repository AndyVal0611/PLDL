import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Class for GUI components
class DesignGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Se-ri's Payroll Form")
        self.window.geometry('855x969')
        self.window.configure(bg='#edecea')

    def label(self, text, x, y, font=('Segoe UI', 10), width=None, bg_color='#edecea', fg_color=None, anchor=None):
        lbl = Label(self.window, text=text, font=font, bg=bg_color, fg=fg_color, anchor=anchor)
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = Entry(self.window, width=width)
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=10, command=None, bg='light gray', fg='white'):
        btn = Button(self.window, text=text, width=width, command=command, font=('Segoe UI', 7, 'bold'), bg=bg, fg=fg)
        btn.place(x=x, y=y)

    def frame(self, x, y, w, h):
        frame = Frame(self.window, width=w, height=h, bg='#f6f6f6')
        frame.place(x=x, y=y)
        return frame

    def add_image(self, x, y, image_path, width=100, height=100):
        img = Image.open(image_path)
        img = img.resize((width, height))
        photo = ImageTk.PhotoImage(img)
        label = Label(self.window, image=photo)
        label.image = photo
        label.place(x=x, y=y)