import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class DesignGUI:
    def __init__(self, window):
        self.window = window
        self.window.configure(bg="#F8D0C0")  # Light pastel pink background

    def label(self, text, x, y, font=("Arial", 10), width=None, fg="#6E2C65"):
        lbl = Label(self.window, text=text, font=font, bg="#F8D0C0", fg=fg)
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = Entry(self.window, width=width, font=("Arial", 10), fg="#6E2C65", bd=2, relief="solid",
                    highlightbackground="#FFB6C1", highlightcolor="#FFB6C1")
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=10, command=None, bg="#FFB6C1", fg="black"):
        btn = Button(self.window, text=text, width=width, command=command, font=("Arial", 10, "bold"),
                     bg=bg, fg=fg, bd=2, relief="solid", highlightbackground="#FFB6C1", highlightcolor="#FFB6C1")
        btn.place(x=x, y=y)

    def frame(self, x, y, w, h):
        frame = Frame(self.window, width=w, height=h, bg="#FFD1DC", bd=2, relief="solid",
                      highlightbackground="#FFB6C1", highlightcolor="#FFB6C1")
        frame.place(x=x, y=y)
        return frame

    def add_image(self, x, y, image_path, width=100, height=100):
        img = Image.open(image_path)
        img = img.resize((width, height))  # Resize image to fit the frame
        photo = ImageTk.PhotoImage(img)

        # Label to display the image
        label = Label(self.window, image=photo, bg="#F8D0C0")
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.place(x=x, y=y)