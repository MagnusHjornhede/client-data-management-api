import sqlite3

from faker import Faker


def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')

    # Create an instance of the Faker class
    fake = Faker()

    # Generate and insert 50 fake entries
    for _ in range(50):
        name = fake.name()
        email = fake.email()
        cursor.execute('INSERT INTO clients (name, email) VALUES (?, ?)', (name, email))

    # Commit the changes to the database
    conn.commit()

    # Fetch data from the table
    cursor.execute('SELECT * FROM clients')
    rows = cursor.fetchall()

    # Print the retrieved data
    for row in rows:
        print(f'ID: {row[0]}, Name: {row[1]}, Email: {row[2]}')

    # Close the database connection
    conn.close()


if __name__ == '__main__':
    main()
