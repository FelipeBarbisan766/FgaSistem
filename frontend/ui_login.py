import tkinter as tk
from tkinter import messagebox
import controllers.auth_controller as auth

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Username").pack(pady=10)
        self.user_entry = tk.Entry(self)
        self.user_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=10)
        self.pass_entry = tk.Entry(self, show="*")
        self.pass_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.login).pack(pady=20)
        self.master = master

    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        if auth.login(username, password):
            self.master.show_frame("HomeFrame")
        else:
            messagebox.showerror("Erro de login", "Usuário ou senha Erados.")