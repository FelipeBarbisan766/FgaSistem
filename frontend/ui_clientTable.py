
import tkinter as tk
import controllers.client_controller as controller

class ClientFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        clients = self.get()
        tk.Label(self, text="Bem-vindo à tela de Clientes!").pack(pady=20)
        tk.Button(self, text="Adicionar Cliente", command=lambda: master.show_frame("AddClientFrame")).pack(pady=10)
        
        for r in clients: 
            id,name,address,email,phone = r
            tk.Label(self, text=f"ID: {id} — Nome: {name} — Endereço: {address} — Email: {email} — Telefone: {phone} ").pack(pady=5)
            
        tk.Button(self, text="Voltar para Home", command=lambda: master.show_frame("HomeFrame")).pack(pady=10)
    
    def get(self):
        clients = controller.get_clients()
        return clients
        
    
    