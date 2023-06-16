import sqlite3

from faker import Faker


def create_database():
    # Connect to the SQLite database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_areas (
            area_id INTEGER PRIMARY KEY AUTOINCREMENT,
            area_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            area_id INTEGER,
            FOREIGN KEY (area_id) REFERENCES customer_areas(area_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            note_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            note TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contracts (
            contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            contract_details TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_details (
            detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            address TEXT,
            phone TEXT,
            email TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            invoice_date TEXT,
            total_amount REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def create_fake_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # Create an instance of the Faker class
    fake = Faker()

    # Generate and insert 50 fake data entries
    for _ in range(50):
        # Generate fake data for each table
        area_name = fake.word()
        customer_name = fake.name()
        note = fake.sentence()
        contract_details = fake.text(max_nb_chars=200)
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()
        invoice_date = fake.date()
        total_amount = fake.random_int(min=100, max=1000)

        # Insert data into the tables
        cursor.execute('INSERT INTO customer_areas (area_name) VALUES (?)', (area_name,))
        area_id = cursor.lastrowid

        cursor.execute('INSERT INTO customers (customer_name, area_id) VALUES (?, ?)', (customer_name, area_id))
        customer_id = cursor.lastrowid

        cursor.execute('INSERT INTO notes (customer_id, note) VALUES (?, ?)', (customer_id, note))

        cursor.execute('INSERT INTO contracts (customer_id, contract_details) VALUES (?, ?)', (customer_id, contract_details))

        cursor.execute('INSERT INTO customer_details (customer_id, address, phone, email) VALUES (?, ?, ?, ?)',
                       (customer_id, address, phone, email))

        cursor.execute('INSERT INTO invoices (customer_id, invoice_date, total_amount) VALUES (?, ?, ?)',
                       (customer_id, invoice_date, total_amount))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def print_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # Fetch data from the tables
    cursor.execute('SELECT * FROM customer_areas')
    areas = cursor.fetchall()

    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()

    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()

    cursor.execute('SELECT * FROM contracts')
    contracts = cursor.fetchall()

    cursor.execute('SELECT * FROM customer_details')
    details = cursor.fetchall()

    cursor.execute('SELECT * FROM invoices')
    invoices = cursor.fetchall()

    # Print the retrieved data
    print("Customer Areas:")
    for area in areas:
        print(f"Area ID: {area[0]}, Area Name: {area[1]}")
    print()

    print("Customers:")
    for customer in customers:
        print(f"Customer ID: {customer[0]}, Customer Name: {customer[1]}, Area ID: {customer[2]}")
    print()

    print("Notes:")
    for note in notes:
        print(f"Note ID: {note[0]}, Customer ID: {note[1]}, Note: {note[2]}")
    print()

    print("Contracts:")
    for contract in contracts:
        print(f"Contract ID: {contract[0]}, Customer ID: {contract[1]}, Contract Details: {contract[2]}")
    print()

    print("Customer Details:")
    for detail in details:
        print(f"Detail ID: {detail[0]}, Customer ID: {detail[1]}, Address: {detail[2]}, Phone: {detail[3]}, Email: {detail[4]}")
    print()

    print("Invoices:")
    for invoice in invoices:
        print(f"Invoice ID: {invoice[0]}, Customer ID: {invoice[1]}, Invoice Date: {invoice[2]}, Total Amount: {invoice[3]}")
    print()

    # Close the database connection
    conn.close()


if __name__ == '__main__':
    #  create_database()
    # create_fake_data()
    print_data()