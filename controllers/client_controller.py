from database import db_clients

def get_clients():
    clients = db_clients.search_clients()
    return clients

def post_client(name, address, phone, email):
    name = name.upper()
    address = address.upper()
    email = email.lower()
    return db_clients.insert_client(name, address, phone, email)