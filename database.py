import sqlite3


def connect_db():
    # connect to database
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    # create table
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS expenses (
    
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT
    
            )
    
        """)

    conn.commit()
    conn.close()


