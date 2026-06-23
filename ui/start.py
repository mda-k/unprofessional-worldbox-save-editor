import customtkinter as ctk

def choose_ui():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.title("WorldBox save editor")
    app.geometry("400x300")
    fuckme = ctk.CTkLabel(master=app, text="hello, world!")
    fuckme.pack()
    app.mainloop()