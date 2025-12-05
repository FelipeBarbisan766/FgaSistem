from database.db_manager import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()
conn.close()

    