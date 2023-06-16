import sqlite3


def setup_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')

    # Insert data into the table
    cursor.execute('''
        INSERT INTO clients (name, email) VALUES (?, ?)
    ''', ('John Doe', 'john.doe@example.com'))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()
