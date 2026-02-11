import tkinter as tk
from tkinter import messagebox
import controllers.client_controller as controller

class AddClientFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Adicionar Cliente").pack(pady=20)
        
        tk.Label(self, text="Nome:").pack(pady=5) 
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        tk.Label(self, text="Endereço:").pack(pady=5) 
        self.address_entry = tk.Entry(self)
        self.address_entry.pack(pady=5)
        tk.Label(self, text="Telefone:").pack(pady=5) 
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack(pady=5)
        tk.Label(self, text="E-mail:").pack(pady=5) 
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Button(self, text="Salvar", command=self.save_client).pack(pady=10)
            
        tk.Button(self, text="Voltar", command=lambda: master.show_frame("ClientFrame")).pack(pady=10)
    
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def save_client(self):
        try:
            name = self.name_entry.get().strip()
            if not name:
                raise ValueError("Nome obrigatório.")

            address = self.address_entry.get().strip()
            phone = self.phone_entry.get().strip()
            email = self.email_entry.get().strip()
        except ValueError as e:
            messagebox.showerror("Erro de entrada", f"Entrada inválida: {e}")
            return

        try:
            result = controller.post_client(name, address, phone, email)
            if result is True:
                messagebox.showinfo("Sucesso", "Cliente adicionado.")
                self.clear_form()
                self.master.show_frame("ClientFrame")
            else:
                messagebox.showerror("Erro", f"Falha adicionar cliente: {result}")
        except Exception as ex:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar: {ex}")