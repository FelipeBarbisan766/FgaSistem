
import tkinter as tk
import controllers.clean_controller as controller

class CleanFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        cleans = self.get()
        tk.Label(self, text="Bem-vindo à tela de limpezas!").pack(pady=20)
        tk.Button(self, text="Adicionar Limpeza", command= self.add).pack(pady=10)
        
        for r in cleans: 
            id, date, price, quantity, unitPrice, status, clientName = r 
            tk.Label(self, text=f"ID: {id} — Data: {date} — Preço: R$ {price:.2f} — Quantidade: {quantity} — Preço Unitário: R$ {unitPrice:.2f} — Status: {status} — Cliente: {clientName} ").pack(pady=5) 
            
        tk.Button(self, text="Voltar para Home", command=lambda: master.show_frame("HomeFrame")).pack(pady=10)
    
    def get(self):
        cleans = controller.get_cleans()
        return cleans
        
    def add(self):
        pass
    