
import tkinter as tk
import controllers.client_controller as controller

class ClientFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Bem-vindo à tela de Clientes!").pack(pady=20)
        tk.Button(self, text="Adicionar Cliente", command=lambda: master.show_frame("AddClientFrame")).pack(pady=10)
        
        self.list_container = tk.Frame(self)
        self.list_container.pack(fill="both", expand=True, padx=10, pady=5)

        tk.Button(self, text="Voltar para Home", command=lambda: master.show_frame("HomeFrame")).pack(pady=10)
    
        self.refresh()

    def refresh(self):
        for w in self.list_container.winfo_children():
            w.destroy()
        clients = controller.get_clients()
        if not clients:
            tk.Label(self.list_container, text="Nenhum cliente encontrado.").pack(pady=5)
            return
        for r in clients:
            id, name, address, email, phone = r
            text = (f"ID: {id} — Nome: {name} — Endereço: {address} — Email: {email} — Telefone: {phone}")
            tk.Label(self.list_container, text=text, anchor="w", justify="left").pack(fill="x", pady=2)
            
        
    
    