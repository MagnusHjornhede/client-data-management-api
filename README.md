# Client Data Management

Client Data Management is a lightweight web application built with **Flask** and **SQLite** for managing structured client information.

The application demonstrates a simple backend architecture combining:

- REST-style routing
- CRUD database operations
- relational data management
- server-side rendering with Flask

The system allows users to view and manage data related to client areas, customers, notes, contracts, details, and invoices.

<br>

## Features

The application provides multiple views for browsing client-related data.

### Client Areas
Displays a table of client areas including:

- area ID
- area name

### Customers
Shows customer information such as:

- customer ID
- customer name
- contact information

### Notes
Displays notes associated with clients including:

- timestamps
- note details

### Contracts
Provides contract records including:

- contract ID
- start date
- end date

### Details
Displays extended customer information:

- addresses
- phone numbers

### Invoices
Shows invoice data including:

- invoice ID
- invoice amount
- due date

<br>

## Technology Stack

- **Python**
- **Flask**
- **SQLite**

<br>

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3 or above)
- Flask (install with `pip install flask`)
- SQLite (included with Python)

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/client-data-management.git`
2. Navigate to the project directory: `cd client-data-management`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`
5. Open your web browser and visit `http://localhost:5000` to access the application.

## Database

The application uses an SQLite database (`clients.db`) to store and retrieve client data. The database schema includes tables for client areas, customers, notes, contracts, details, and invoices. You can modify the database structure by editing the `clients.sql` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
