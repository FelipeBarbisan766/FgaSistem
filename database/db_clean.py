from database.db_manager import get_connection

def search_clean_paginated(limit: int, offset: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT cleans.id, cleans.date, cleans.price, cleans.quantity, cleans.unitPrice, cleans.status, clients.name
        FROM cleans
        LEFT JOIN clients ON cleans.clientId = clients.id
        ORDER BY cleans.id
        LIMIT ? OFFSET ?;
        """,
        (limit, offset),
    )
    return cursor.fetchall()

def count_clean():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM cleans;")
    (total,) = cursor.fetchone()
    return total

def search_clean():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT cleans.id, cleans.date, cleans.price, cleans.quantity, cleans.unitPrice, cleans.status, clients.name
        FROM cleans
        LEFT JOIN clients ON cleans.clientId = clients.id
        ORDER BY cleans.id;
        """
    )
    return cursor.fetchall()

def insert_clean(date, price, quantity, unitPrice, status, clientID):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cleans (date, price, quantity, unitPrice, status, clientId) VALUES (?, ?, ?, ?, ?, ?);",
        (date, price, quantity, unitPrice, status, clientID),
    )
    conn.commit()
    return True

def remove_clean(clean_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cleans WHERE id = ?;", (clean_id,))
    conn.commit()
    return True