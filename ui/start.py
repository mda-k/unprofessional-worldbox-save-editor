import customtkinter as ctk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from pathlib import Path

def choose_ui():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    def FUCKMYLIFE():
        app.quit()
        app.destroy()
    app.protocol("WM_DELETE_WINDOW", FUCKMYLIFE)
    app.title("unprofessional worldbox save editor")
    app.geometry("672x250")
    app.resizable(False, False)
    app.configure(fg_color="black")
    fold0 = os.path.dirname(__file__)
    fold1 = os.path.join(fold0, "uwse_logo.png")
    fold2 = os.path.join(fold0, "uwse_logo_small_ico.ico")

    try:
        app.iconbitmap(fold2)
    except Exception:
        messagebox.showerror("mild error i guess", "the unprofessional branding icon (/resources/uwse_logo_small_ico.png) is missing i think.")
    try:
        pillow_img = Image.open(fold1)
    except FileNotFoundError:
        messagebox.showerror("mild error i guess", "the unprofessional branding image (/resources/uwse_logo.png) is missing i think.")
        pillow_img = Image.new("RGB", (200, 200), color="gray")
    top = ctk.CTkImage(light_image=pillow_img, dark_image=pillow_img, size=(672, 186))
    packertop = ctk.CTkLabel(master=app, image=top, text="")
    packertop.pack()
    welcome = ctk.CTkLabel(master=app, wraplength=650, justify="left", text_color="#960101", text="welcome to the unprofessional worldbox save editor by md! this beginner inefficient, inconvenient program will decompile your .wbox save to a readable. json file. to start, this piece of shit program needs you to choose a .wbox file.", font=("Palatino Linotype", 12, "bold"))
    welcome.pack()
    app.mainloop()
    
    
