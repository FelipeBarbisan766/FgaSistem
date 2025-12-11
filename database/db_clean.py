from database.db_manager import get_connection

def search_cleans():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT cleans.id, cleans.date, cleans.price, cleans.quantity, cleans.unitPrice, cleans.status, clients.name FROM cleans LEFT JOIN clients ON cleans.clientId = clients.id;")
    return cursor.fetchall()