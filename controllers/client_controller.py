from database import db_clients

def get_clients():
    clients = db_clients.search_clients()
    return clients