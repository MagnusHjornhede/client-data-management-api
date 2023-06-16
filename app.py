from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data(table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # Fetch data from the specified table
    cursor.execute(f'SELECT * FROM {table_name}')
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the retrieved data
    return data


@app.route('/')
def index():
    # Get the data from the database
    areas = get_data('customer_areas')
    customers = get_data('customers')
    notes = get_data('notes')
    contracts = get_data('contracts')
    details = get_data('customer_details')
    invoices = get_data('invoices')

    # Render the template with the data
    return render_template('index.html', areas=areas, customers=customers, notes=notes,
                           contracts=contracts, details=details, invoices=invoices)


@app.route('/areas')
def areas():
    areas_data = get_data('customer_areas')
    return render_template('areas.html', areas=areas_data)


@app.route('/customers')
def customers():
    customers_data = get_data('customers')
    return render_template('customers.html', customers=customers_data)


@app.route('/notes')
def notes():
    notes_data = get_data('notes')
    return render_template('notes.html', notes=notes_data)


@app.route('/contracts')
def contracts():
    contracts_data = get_data('contracts')
    return render_template('contracts.html', contracts=contracts_data)


@app.route('/details')
def details():
    details_data = get_data('customer_details')
    customers_data = get_data('customers')
    return render_template('details.html', details=details_data, customers=customers_data)


@app.route('/invoices')
def invoices():
    invoices_data = get_data('invoices')
    return render_template('invoices.html', invoices=invoices_data)


if __name__ == '__main__':
    app.run()
