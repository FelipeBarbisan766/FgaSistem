from database.db_manager import get_connection

def search_clients_paginated(limit: int, offset: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT clients.id, clients.name, clients.address, clients.email, clients.phone
        FROM clients
        ORDER BY clients.id
        LIMIT ? OFFSET ?;
        """,
        (limit, offset),
    )
    return cursor.fetchall()

def count_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM clients;")
    (total,) = cursor.fetchone()
    return total

def search_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT clients.id, clients.name, clients.address, clients.email, clients.phone
        FROM clients
        ORDER BY clients.id;
        """
    )
    return cursor.fetchall()

def insert_client(name, address, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clients (name, address, phone, email) VALUES (?, ?, ?, ?);",
        (name, address, phone, email),
    )
    conn.commit()
    return True