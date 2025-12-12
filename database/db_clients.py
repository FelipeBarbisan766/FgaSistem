from database.db_manager import get_connection
def search_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT clients.id, clients.name,clients.address, clients.email, clients.phone FROM clients;")
    return cursor.fetchall()