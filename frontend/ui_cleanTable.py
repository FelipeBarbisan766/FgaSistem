import tkinter as tk
import controllers.clean_controller as controller

class CleanFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Bem-vindo à tela de limpezas!").pack(pady=20)
        tk.Button(self, text="Adicionar Limpeza", command=lambda: master.show_frame("AddCleanFrame")).pack(pady=10)

        self.list_container = tk.Frame(self)
        self.list_container.pack(fill="both", expand=True, padx=10, pady=5)

        tk.Button(self, text="Voltar para Home", command=lambda: master.show_frame("HomeFrame")).pack(pady=10)
        
        self.refresh()

    def refresh(self):
        for w in self.list_container.winfo_children():
            w.destroy()
        cleans = controller.get_cleans()
        if not cleans:
            tk.Label(self.list_container, text="Nenhuma limpeza encontrada.").pack(pady=5)
            return
        for r in cleans:
            id, date, price, quantity, unitPrice, status, clientName = r
            text = (f"ID: {id} — Data: {date} — Preço: R$ {price:.2f} — "
                    f"Quantidade: {quantity} — Preço Unitário: R$ {unitPrice:.2f} — "
                    f"Status: {status} — Cliente: {clientName}")
            tk.Label(self.list_container, text=text, anchor="w", justify="left").pack(fill="x", pady=2)
