# Inventory Management System

## Introduction

An inventory management system built using Python, SQLAlchemy, SQLite, and Alembic. This project features a command-line interface (CLI) for managing products, customers, suppliers, sales, and sales details. It allows listing products, managing inventory, handling suppliers and customers, and keeping track of sales and related details.

## Features

-Manage products, customers, suppliers, and sales.
-Maintain stock levels and update product quantities.
-Keep track of sales and customer details.
-Use Alembic to handle database migrations.
-Seed the database with fake data using the Faker library.
-SQLite is used as the default database for simplicity.

## Installation

## Prerequisites

-Python 3.8+
-Pip (Python package manager)

## Setup

1. Clone the repository:

    git clone <https://github.com/aggreyrc/Phase-3-project-Stock-Inventory/tree/master>
    cd inventory

2. Install dependencies:

    pip install -r requirements.txt

3. Setup the database: Initialize the database and create all tables using Alembic migrations:

    alembic upgrade head

4. Seed the database : You can use the provided seed.py script to populate the tables with fake data using the Faker library:

    python seed.py

## Database Models

The project includes the following database models defined in SQLAlchemy:

1. Product: Represents a product with fields like name, price, category, quantity, and supplier reference.
2. Customer: Represents a customer with details like name, phone, email, and address.
3. Supplier: Represents a supplier with fields like name, phone number, email, and address.
4. Sale: Represents a sale with fields like sale date, total amount, and a reference to the customer.
5. SaleDetail: Represents details of a sale, including the product sold, quantity, and price.
These models include validations to ensure data integrity (e.g., NOT NULL constraints, length limits).

## CLI Commands

The CLI is implemented in cli.py and provides the following functionalities:

0. Exit the program:
Exits the CLI.
Command: 0

1. List all products:
Lists all products available in the database.
Command: 1

2. Find Product By name:
Searches for a product by name.
Command: 2

3. Find product by id:
Searches for a product by id.
Command: 3

## Usage

To use the inventory management system, simply run the cli.py file:

    python cli.py

## Migrations

We use Alembic for managing database migrations. If you need to make schema changes (like adding new fields or constraints), follow these steps:

1. Create a new migration:

    alembic revision --autogenerate -m "Migration message"

2. Apply the migration:

    alembic upgrade head

3. To downgrade:

    alembic downgrade -1
