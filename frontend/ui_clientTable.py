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

        self.search_visible = False
        self.search_var = tk.StringVar()

        self.search_bar = tk.Frame(self)
        tk.Label(self.search_bar, text="Pesquisar:").pack(side="left")
        self.search_entry = tk.Entry(self.search_bar, textvariable=self.search_var, width=40)
        self.search_entry.pack(side="left", padx=6)

        tk.Button(self.search_bar, text="Limpar", command=self.clear_search).pack(side="left")

        self.search_var.trace_add("write", lambda *_: self.on_search_change())

        self.search_entry.bind("<Escape>", lambda e: self.hide_search())

        # --- Paginação ---
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

        self.bind_all("<Key>", self.global_key_listener)

        self.refresh()

    # -------------------------
    # Busca: mostrar/esconder
    # -------------------------
    def show_search(self):
        if not self.search_visible:
            self.search_bar.pack(fill="x", padx=10, pady=(0, 6), before=self.list_container)
            self.search_visible = True
        self.search_entry.focus_set()
        self.search_entry.icursor("end")

    def hide_search(self):
        if self.search_visible:
            self.search_bar.pack_forget()
            self.search_visible = False
        self.search_var.set("")  
        self.list_container.focus_set()

    def clear_search(self):
        self.search_var.set("")
        self.search_entry.focus_set()

    def on_search_change(self):
        self.page = 0
        self.refresh()

    def global_key_listener(self, event):
        w = self.focus_get()
        if isinstance(w, tk.Entry):
            return

        if event.state & 0x4:  
            return

        if event.char and event.char.isprintable() and not event.char.isspace():
            self.show_search()
            self.search_var.set(event.char)
            self.search_entry.icursor("end")

        if event.keysym == "slash":
            self.show_search()
            return

    # -------------------------
    # Paginação
    # -------------------------
    def prev_page(self):
        if self.page > 0:
            self.page -= 1
            self.refresh()

    def next_page(self):
        total = self.get_total_current_mode()
        if total <= 0:
            return
        max_page = (total - 1) // self.page_size
        if self.page < max_page:
            self.page += 1
            self.refresh()

    def get_total_current_mode(self):
        q = self.search_var.get().strip()
        if q:
            return controller.get_clients_total_filtered(q)  
        return controller.get_clients_total()

    def get_page_current_mode(self):
        q = self.search_var.get().strip()
        if q:
            return controller.get_clients_page_filtered(q, self.page, self.page_size)  
        return controller.get_clients_page(self.page, self.page_size)

    def refresh(self):
        for w in self.list_container.winfo_children():
            w.destroy()

        try:
            total = self.get_total_current_mode()
            if total <= 0:
                tk.Label(self.list_container, text="Nenhum cliente encontrado.").pack(pady=5)
                self.prev_btn.config(state="disabled")
                self.next_btn.config(state="disabled")
                self.page_label.config(text="")
                return

            max_page = (total - 1) // self.page_size
            if self.page > max_page:
                self.page = max_page

            clients = self.get_page_current_mode()

        except AttributeError:
            tk.Label(
                self.list_container,
                text="Erro Ao carregar clientes."
            ).pack(pady=5)
            return

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
        self.hide_search()

    def remove_client(self, client_id):
        controller.delete_client(client_id)
        self.refresh()