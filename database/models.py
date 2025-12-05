from .db_manager import get_connection

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arquivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            path TEXT NOT NULL,
            date_upload TEXT NOT NULL,
            shooterId INTERGER NOT NULL,
            FOREIGN KEY (shooterId) REFERENCES shooter(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS year (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year NUMBER NOT NULL,
            instructor TEX NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS servedYear (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            shooterId INTERGER NOT NULL,
            yearId INTERGER NOT NULL,
            FOREIGN KEY (yearId) REFERENCES year(id),
            FOREIGN KEY (shooterId) REFERENCES shooter(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS shooter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ra NUMBER UNIQUE NOT NULL,
            number NUMBER UNIQUE,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            cpf NUMBER UNIQUE,
            phone NUMBER UNIQUE
        )
    ''')

    conn.commit()
    conn.close()
