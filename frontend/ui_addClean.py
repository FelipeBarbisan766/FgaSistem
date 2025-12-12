import tkinter as tk
import controllers.clean_controller as controller

class AddCleanFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Adicionar Nova Limpeza").pack(pady=20)
        
        tk.Label(self, text="Data:").pack(pady=5) 
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(pady=5)
        tk.Label(self, text="Preço:").pack(pady=5) 
        self.price_entry = tk.Entry(self)
        self.price_entry.pack(pady=5)
        tk.Label(self, text="Quantidade:").pack(pady=5) 
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack(pady=5)
        tk.Label(self, text="Preço Unitário:").pack(pady=5) 
        self.unitPrice_entry = tk.Entry(self)
        self.unitPrice_entry.pack(pady=5)
        tk.Label(self, text="Status:").pack(pady=5) 
        self.status_entry = tk.Entry(self)
        self.status_entry.pack(pady=5)
        tk.Label(self, text="Cliente:").pack(pady=5) 
        self.client_entry = tk.Entry(self)
        self.client_entry.pack(pady=5)

        tk.Button(self, text="Salvar Limpeza", command=self.save_clean).pack(pady=10)
            
        tk.Button(self, text="Voltar", command=lambda: master.show_frame("CleanFrame")).pack(pady=10)
    
    def save_clean(self):
        date = self.date_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        unitPrice = float(self.unitPrice_entry.get())
        status = self.status_entry.get()
        clientID = int(self.client_entry.get())
        cleans = controller.post_clean(date, price, quantity, unitPrice, status, clientID)
        if cleans == True:
            self.master.show_frame("CleanFrame")