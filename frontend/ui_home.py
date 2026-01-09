import tkinter as tk

class HomeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Bem-vindo à tela principal!").pack(pady=20)
        tk.Button(self, text="Limpezas", command=lambda: master.show_frame("CleanFrame")).pack(pady=10)
        tk.Button(self, text="Clientes", command=lambda: master.show_frame("ClientFrame")).pack(pady=10)
        tk.Button(self, text="Sair", command=lambda: master.show_frame("LoginFrame")).pack(pady=10)