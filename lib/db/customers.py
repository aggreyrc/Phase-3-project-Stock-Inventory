from models import Customer, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Customer Functions

# listing all customers
def list_all_customers():
    try:
        customers = session.query(Customer).all()
        if customers:
            for customer in customers:
                print(f'ID: {customer.customer_id}, Name: {customer.name}')
        else:
            print('No Customers found')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        session.close()
        
# Finding Customer by Name
def find_customer_by_name():
    name = input('Enter the name of the Customer to find: ')
    try:
        customer = session.query(Customer).filter(Customer.name.ilike(f'%{name}%')).first()
        if customer:
            print(f'ID: {customer.customer_id}, Name: {customer.name}, Phone: {customer.phone}')
        else:
            print('Customer not found')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        session.close()
        
        
# FInding Customer by Id
def find_customer_by_id():
    id_ = input("Enter the Customer's id: ")
    customer = session.query(Customer).filter_by(customer_id=id_).first()
    if customer:
         print(f'ID: {customer.customer_id}, Name: {customer.name}')
    else:
        print('Customer not found')
        
        
# Create Customer
def create_customer():
    name = input("Enter Customer's name: ")
    phone = input("Enter Customer's Phone Number: ")
    email = input("Enter Customer's email: ")
    address = input("Enter Customer's address: ")
    try:
        new_customer = Customer(name=name, phone=phone, email=email,address=address)
        session.add(new_customer)
        session.commit()
        print("Customer added successfully")
    except Exception as exc:
        print(f"An error occurred: {exc}")
        
# Update a Customer's address
def update_customer():
    id_ = input("Enter the Customer's id: ")
    new_address = input("Enter new address: ")
    try:
        customer = session.query(Customer).filter_by(customer_id=id_).first()
        if customer:
            customer.address = new_address
            session.commit()
            print("Customer updated successfully")
        else:
            print("Customer not found")
    except Exception as exc:
        print(f"An error occurred: {exc}")
        
# Delete Customer
def delete_customer():
    id_ = input("Enter the Customer's id: ")
    try:
        customer = session.query(Customer).filter_by(customer_id=id_).first()
        if customer:
            session.delete(customer)
            session.commit()
            print("Customer deleted successfully")
        else:
            print("Customer not found")
    except Exception as exc:
        print(f"An error occurred: {exc}")