import tkinter as tk
import controllers.client_controller as controller

class AddClientFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Adicionar Novo Cliente").pack(pady=20)
        
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

        tk.Button(self, text="Salvar Cliente", command=self.save_client).pack(pady=10)
            
        tk.Button(self, text="Voltar", command=lambda: master.show_frame("ClientFrame")).pack(pady=10)
    
    def save_client(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        clients = controller.post_client(name, address, phone, email)
        if clients == True:
            self.master.show_frame("ClientFrame")