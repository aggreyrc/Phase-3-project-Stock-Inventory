from models import Supplier, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Supplier Functions

# listing all Suppliers
def list_all_suppliers():
    try:
        suppliers = session.query(Supplier).all()
        if suppliers:
            for supplier in suppliers:
                print(f'ID: {supplier.supplier_id}, Name: {supplier.name}')
        else:
            print('No Suppliers found')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        session.close()
        
# Finding Supplier by Name
def find_supplier_by_name():
    name = input('Enter the name of the Supplier to find: ')
    try:
        supplier = session.query(Supplier).filter(Supplier.name.ilike(f'%{name}%')).first()
        if supplier:
            print(f'ID: {supplier.supplier_id}, Name: {supplier.name}, Phone: {supplier.phone_number}')
        else:
            print('Supplier not found')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        session.close()
        
        
# FInding Supplier by Id
def find_supplier_by_id():
    id_ = input("Enter the Supplier's id: ")
    supplier = session.query(Supplier).filter_by(supplier_id=id_).first()
    if supplier:
         print(f'ID: {supplier.supplier_id}, Name: {supplier.name}')
    else:
        print('Supplier not found')
        
        
# Create Supplier
def create_supplier():
    name = input("Enter Supplier's name: ")
    phone = input("Enter Supplier's Phone Number: ")
    email = input("Enter Supplier's email: ")
    address = input("Enter Supplier's address")
    try:
        new_Supplier = Supplier(name=name, phone_number=phone, email=email, address=address)
        session.add(new_Supplier)
        session.commit()
        print("Supplier added successfully")
    except Exception as exc:
        print(f"An error occurred: {exc}")
        
# Update a Supplier's Phone
def update_supplier():
    id_ = input("Enter the Supplier's id: ")
    new_phone = input("Enter new phone: ")
    try:
        supplier = session.query(Supplier).filter_by(supplier_id=id_).first()
        if supplier:
            supplier.phone_number = new_phone
            session.commit()
            print("Supplier updated successfully")
        else:
            print("Supplier not found")
    except Exception as exc:
        print(f"An error occurred: {exc}")
        
# Delete Supplier
def delete_supplier():
    id_ = input("Enter the Supplier's id: ")
    try:
        supplier = session.query(Supplier).filter_by(supplier_id=id_).first()
        if supplier:
            session.delete(supplier)
            session.commit()
            print("Supplier deleted successfully")
        else:
            print("Supplier not found")
    except Exception as exc:
        print(f"An error occurred: {exc}")