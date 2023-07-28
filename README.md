# Banking Database
A banking database implemented in SQL, with appropriate functionality to modulate the database entries. The database contains tables for customers, accounts, loans, and transactions related to a fictional bank.

## Database Setup

The SQL code starts by creating a database named `bankdatabase` if it does not already exist. This will be the main database to hold all the bank-related information.

## Table Setup

### Customer Table

The `customer` table stores information about bank customers. It has the following columns:

- `CustomerID` (Primary Key, Auto Increment): Unique identifier for each customer.
- `FirstName`: The first name of the customer.
- `LastName`: The last name of the customer.
- `DateOfBirth`: The date of birth of the customer.
- `HomeAddress`: The home address of the customer.
- `Phone`: The phone number of the customer.

### Account Table

The `account` table represents bank accounts. It includes the following columns:

- `AccountID` (Primary Key, Auto Increment): Unique identifier for each account.
- `Balance`: The current balance of the account (floating-point number with two decimal places).
- `SortCode`: The sort code of the account with a default value of '05-00-05'.
- `CustomerID`: The foreign key referencing the `CustomerID` column in the `customer` table.

### Loan Table

The `loan` table stores information about loans taken by bank customers. It has the following columns:

- `LoanID` (Primary Key, Auto Increment): Unique identifier for each loan.
- `LoanAmount`: The amount of the loan (floating-point number with two decimal places).
- `CustomerID`: The foreign key referencing the `CustomerID` column in the `customer` table.
- `AccountID`: The foreign key referencing the `AccountID` column in the `account` table.
- `PaymentRate`: The monthly payment rate for the loan (floating-point number with two decimal places).
- `NumberOfMonthlyPayments`: The number of monthly payments required for the loan.
- `FirstPaymentDate`: The date of the first loan payment.
- `MonthlyDueDate`: The preferred monthly due date for payments with a default value of '1st'.

### Transaction Table

The `transaction` table stores details of transactions made on bank accounts. It includes the following columns:

- `TransactionID` (Primary Key, Auto Increment): Unique identifier for each transaction.
- `TransactionAmount`: The amount of the transaction (floating-point number with two decimal places).
- `TransactionType`: The type of the transaction (e.g., Incoming or Outgoing).
- `TransactionDate`: The date of the transaction.
- `Reference`: An optional reference for the transaction.
- `AccountID`: The foreign key referencing the `AccountID` column in the `account` table.

## Data Insertion

The SQL code also includes data insertion statements to populate the tables with sample data for customers, accounts, loans, and transactions. The sample data is used for testing and demonstration purposes.

Feel free to use this SQL code as a starting point for setting up your bank database or experimenting with SQL queries on bank-related data.

(Note: The sample data provided here is fictional and not based on real bank data.)

**Please make sure to review and modify the SQL code as needed to match your specific requirements and database environment.**

For more information on SQL syntax and database management, refer to the documentation of your specific database management system.
