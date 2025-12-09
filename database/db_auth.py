from database.db_manager import get_connection

def search_user(user):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user, password FROM users WHERE user = ?", (user,))
    return cursor.fetchone()