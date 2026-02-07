from database.db_manager import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            phone TEXT,
            email TEXT
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS cleans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATETIME NOT NULL,
            price DECIMAL,
            quantity INTEGER,
            unitPrice DECIMAL NOT NULL,
            status TEXT NOT NULL,
            clientId INTEGER,
            FOREIGN KEY (clientId) REFERENCES clients(id)
        )
    """
    )

    conn.commit()
    conn.close()
