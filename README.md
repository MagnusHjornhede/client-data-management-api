# Client Data Management

Client Data Management is a web application built with Flask and SQLite for managing client information. It allows you to view and manage data related to client areas, customers, notes, contracts, details, and invoices.

## Features

- View client areas: Displays a table of client areas with their corresponding IDs and area names.
- View customers: Shows a table of customer data, including IDs, names, and contact information.
- View notes: Displays a table of notes related to clients, with timestamps and details.
- View contracts: Shows a table of contract information, including contract IDs, start dates, and end dates.
- View details: Displays customer details, such as IDs, names, addresses, and phone numbers.
- View invoices: Shows a table of invoices associated with clients, including invoice IDs, amounts, and due dates.

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
