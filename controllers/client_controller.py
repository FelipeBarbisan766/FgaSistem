from database import db_clients

def get_clients_page(page: int, page_size: int = 20):
    if page < 0:
        page = 0
    if page_size <= 0:
        page_size = 20

    offset = page * page_size
    return db_clients.search_clients_paginated(limit=page_size, offset=offset)

def get_clients_total():
    return db_clients.count_clients()

def get_clients():
    return db_clients.search_clients()


def get_clients_page_filtered(query: str, page: int, page_size: int = 20):
    if page < 0:
        page = 0
    if page_size <= 0:
        page_size = 20

    offset = page * page_size
    return db_clients.search_clients_paginated_filtered(query=query, limit=page_size, offset=offset)

def get_clients_total_filtered(query: str):
    return db_clients.count_clients_filtered(query=query)

def post_client(name, address, phone, email):
    name = name.upper()
    address = address.upper()
    email = email.lower()
    return db_clients.insert_client(name, address, phone, email)

def delete_client(client_id):
    return db_clients.remove_client(client_id)