
import tkinter as tk

class CleanFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Bem-vindo à tela de limpezas!").pack(pady=20)
        tk.Button(self, text="Adicionar Limpeza", command= self.add).pack(pady=10)
        
        for i in range(5):
            tk.Label(self, text=f"test of table {i+1}").pack(pady=5)
        
        
        
        
        
        tk.Button(self, text="Voltar para Home", command=lambda: master.show_frame("HomeFrame")).pack(pady=10)
    
    
    
    
    def add(self):
        pass
    