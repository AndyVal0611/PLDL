from tkinter import *
from PIL import Image, ImageTk

# Create a class for DesignGUI
class DesignGUI:
    # Initialize the window
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("AV Log-in Page")
        self.windows.geometry('1490x900')
        self.windows.configure(bg='#F9EDED')  # Set the background color of the window

    # Define labels
    def label(self, text, x, y, font=('Century Gothic', 10), width=None, bg_color='#F9EDED', fg_color='#7A0E0E', anchor=None, cursor=None):
        lbl = Label(self.windows, text=text, font=font, bg=bg_color, fg=fg_color, anchor=anchor, cursor=cursor)
        lbl.place(x=x, y=y, width=width)
        return lbl

    # Define textbox
    def entry(self, x, y, width=41, show=None, bg_color='#F4D2D2', fg_color='#7A0E0E'):
        txt = Entry(self.windows, width=width, show=show, font=('Century Gothic', 12), bg=bg_color, fg=fg_color)
        txt.place(x=x, y=y)
        return txt

    # Define Login button
    def button(self, text, x, y, width=10, command=None, bg='#7A0E0E', fg='white', font=('Century Gothic', 12, 'bold')):
        btn = Button(self.windows, text=text, width=width, command=command, font=font, bg=bg, fg=fg)
        btn.place(x=x, y=y)

    # Define frames for outer (border) and inner (main frame contents)
    def frame(self, x, y, w, h, bg_color='#F9EDED'):
        frame = Frame(self.windows, width=w, height=h, bg=bg_color)
        frame.place(x=x, y=y)
        return frame

    # Define by setting the background photo and the logo
    def add_image(self, x, y, image_path, width=100, height=100, bg_color='#F9EDED'):
        img = Image.open(image_path)
        img = img.resize((width, height))
        photo = ImageTk.PhotoImage(img)
        label = Label(self.windows, image=photo, bg=bg_color)
        label.image = photo  # Keep a reference to the image
        label.place(x=x, y=y)