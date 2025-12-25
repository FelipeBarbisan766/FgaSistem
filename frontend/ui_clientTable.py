import tkinter as tk
import controllers.client_controller as controller

class ClientFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Bem-vindo à tela de Clientes!").pack(pady=20)
        tk.Button(
            self,
            text="Adicionar Cliente",
            command=lambda: master.show_frame("AddClientFrame"),
        ).pack(pady=10)

        self.page_size = 20
        self.page = 0  

        self.list_container = tk.Frame(self)
        self.list_container.pack(fill="both", expand=True, padx=10, pady=5)

        self.pagination_bar = tk.Frame(self)
        self.pagination_bar.pack(fill="x", padx=10, pady=5)

        self.prev_btn = tk.Button(self.pagination_bar, text="◀ Anterior", command=self.prev_page)
        self.prev_btn.pack(side="left")

        self.page_label = tk.Label(self.pagination_bar, text="")
        self.page_label.pack(side="left", padx=10)

        self.next_btn = tk.Button(self.pagination_bar, text="Próximo ▶", command=self.next_page)
        self.next_btn.pack(side="left")

        tk.Button(
            self,
            text="Voltar para Home",
            command=lambda: master.show_frame("HomeFrame"),
        ).pack(pady=10)

        self.refresh()

    def prev_page(self):
        if self.page > 0:
            self.page -= 1
            self.refresh()

    def next_page(self):
        total = controller.get_clients_total()
        if total <= 0:
            return

        max_page = (total - 1) // self.page_size
        if self.page < max_page:
            self.page += 1
            self.refresh()

    def refresh(self):
        for w in self.list_container.winfo_children():
            w.destroy()

        total = controller.get_clients_total()

        if total <= 0:
            tk.Label(self.list_container, text="Nenhum cliente encontrado.").pack(pady=5)
            self.prev_btn.config(state="disabled")
            self.next_btn.config(state="disabled")
            self.page_label.config(text="")
            return

        max_page = (total - 1) // self.page_size

        if self.page > max_page:
            self.page = max_page

        clients = controller.get_clients_page(self.page, self.page_size)

        for r in clients:
            id, name, address, email, phone = r
            text = f"ID: {id} — Nome: {name} — Endereço: {address} — Email: {email} — Telefone: {phone}"
            tk.Label(self.list_container, text=text, anchor="w", justify="left").pack(fill="x", pady=2)
            tk.Button(
                self.list_container,
                text="Remover",
                command=lambda client_id=id: self.remove_client(client_id)
            ).pack(pady=2)

        self.page_label.config(text=f"Página {self.page + 1} de {max_page + 1} (Total: {total})")
        self.prev_btn.config(state=("normal" if self.page > 0 else "disabled"))
        self.next_btn.config(state=("normal" if self.page < max_page else "disabled"))
        
    def on_show(self):
        self.page = 0

    def remove_client(self, client_id):
        controller.delete_client(client_id)
        self.refresh()