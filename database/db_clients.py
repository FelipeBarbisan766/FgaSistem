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

# -----------------------------
# NOVO: busca com filtro + paginação
# -----------------------------
def search_clients_paginated_filtered(query: str, limit: int, offset: int):
    conn = get_connection()
    cursor = conn.cursor()

    q = (query or "").strip()
    like = f"%{q}%"

    # se for número, também tenta bater no ID
    q_int = None
    try:
        q_int = int(q)
    except ValueError:
        q_int = None

    cursor.execute(
        """
        SELECT clients.id, clients.name, clients.address, clients.email, clients.phone
        FROM clients
        WHERE
            (? IS NOT NULL AND clients.id = ?)
            OR clients.name    LIKE ?
            OR clients.address LIKE ?
            OR clients.email   LIKE ?
            OR clients.phone   LIKE ?
        ORDER BY clients.id
        LIMIT ? OFFSET ?;
        """,
        (q_int, q_int, like, like, like, like, limit, offset),
    )
    return cursor.fetchall()

def count_clients_filtered(query: str):
    conn = get_connection()
    cursor = conn.cursor()

    q = (query or "").strip()
    like = f"%{q}%"

    q_int = None
    try:
        q_int = int(q)
    except ValueError:
        q_int = None

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM clients
        WHERE
            (? IS NOT NULL AND clients.id = ?)
            OR clients.name    LIKE ?
            OR clients.address LIKE ?
            OR clients.email   LIKE ?
            OR clients.phone   LIKE ?;
        """,
        (q_int, q_int, like, like, like, like),
    )
    (total,) = cursor.fetchone()
    return total

def insert_client(name, address, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clients (name, address, phone, email) VALUES (?, ?, ?, ?);",
        (name, address, phone, email),
    )
    conn.commit()
    return True

def remove_client(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id = ?;", (client_id,))
    conn.commit()
    return True