import tkinter as tk
from tkinter import messagebox
import controllers.clean_controller as controller

class AddCleanFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Adicionar Limpeza").pack(pady=20)
        
        tk.Label(self, text="Data:").pack(pady=5) 
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(pady=5)

        tk.Label(self, text="Preço:").pack(pady=5) 
        self.price_entry = tk.Entry(self)
        self.price_entry.pack(pady=5)

        tk.Label(self, text="Quantidade:").pack(pady=5) 
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack(pady=5)

        tk.Label(self, text="Status:").pack(pady=5) 
        self.status_entry = tk.Entry(self)
        self.status_entry.pack(pady=5)

        tk.Label(self, text="Cliente:").pack(pady=5) 
        self.client_entry = tk.Entry(self)
        self.client_entry.pack(pady=5)

        tk.Button(self, text="Salvar", command=self.save_clean).pack(pady=10)
        tk.Button(self, text="Voltar", command=lambda: master.show_frame("CleanFrame")).pack(pady=10)
    
    def clear_form(self):
        self.date_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.unitPrice_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)
        self.client_entry.delete(0, tk.END)

    def save_clean(self):
        try:
            date = self.date_entry.get().strip()
            if not date:
                raise ValueError("Data é obrigatória.")

            price = float(self.price_entry.get().strip())
            quantity = int(self.quantity_entry.get().strip())
            unitPrice = float(self.unitPrice_entry.get().strip())
            status = self.status_entry.get().strip()
            clientID = int(self.client_entry.get().strip())
        except ValueError as e:
            messagebox.showerror("Erro de entrada", f"Entrada inválida: {e}")
            return

        try:
            result = controller.post_clean(date, price, quantity, unitPrice, status, clientID)
            if result is True:
                messagebox.showinfo("Sucesso", "Limpeza adicionada com sucesso.")
                self.clear_form()
                self.master.show_frame("CleanFrame")
            else:
                messagebox.showerror("Erro", f"Falha ao adicionar limpeza: {result}")
        except Exception as ex:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar: {ex}")