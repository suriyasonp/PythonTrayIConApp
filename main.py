import sys
from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
import PIL.Image, PIL.ImageDraw
import tkinter as ttk
from tkinter import messagebox
from datetime import datetime

def on_clicked_notify(icon):
    print("Hello")
    icon.notify("Hello World")


def on_clicked_about():
    root = ttk.Tk()
    root.withdraw()
    messagebox.showinfo("About", aboutMessage)


def on_clicked_exit(icon):
    icon.notify("Good bye!")
    icon.stop()


def on_clicked_setting():
    root = ttk.Tk()
    root.title("Settings")

    # Create a frame to hold the widgets
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Create a label and an entry for the token
    token_label = ttk.Label(frame, text="Token:")
    token_label.grid(row=0, column=0, sticky=ttk.W)
    token_entry = ttk.Entry(frame)
    token_entry.grid(row=0, column=1, sticky=ttk.E)

    time_label = ttk.Label(frame, text="Time:")
    time_label.grid(row=1, column=0, sticky=ttk.W)
    time_entry = ttk.Entry(frame)
    time_entry.grid(row=1, column=1, sticky=ttk.E)

    button = ttk.Button(frame, text="Save", command=root.destroy)
    button.grid(row=2, column=0, sticky=ttk.W)

    # Run the main loop
    root.mainloop()


state = False

image = PIL.Image.open("Assets/mail.png")
aboutMessage = ("App: App name\n"
                "App version: 0.1.0\n"
                "Developer: Suriya S.")

tray = icon('test', image, menu=menu(
                                        item('Notify',on_clicked_notify),
                                        item('Setting', on_clicked_setting),
                                        item('About', on_clicked_about),
                                        item('Exit', on_clicked_exit)
                                    )
            )

tray.run()
