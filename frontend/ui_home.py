import tkinter as tk

class HomeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Bem-vindo à tela principal!").pack(pady=20)
        tk.Button(self, text="Logout", command=lambda: master.show_frame("LoginFrame")).pack(pady=10)