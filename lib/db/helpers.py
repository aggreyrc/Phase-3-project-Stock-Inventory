from models import Product, Customer, Supplier, Sale, SaleDetail,session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



def exit_program():
    print('Goodbye')
    exit()
    
    
# Product Functions

# listing all products
def list_all_products():
    try:
        products = session.query(Product).all()
        if products:
            for product in products:
                print(f'ID: {product.id}, Name: {product.name}, Category: {product.category}')
        else:
            print('No products found')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        session.close()
        
# Finding Product by Name
def find_product_by_name():
    name = input('Enter the name of the product to find: ')
    try:
        product = session.query(Product).filter_by(name=name).first()
        if product:
            print(f'ID: {product.id}, Name: {product.name}, Category: {product.category}')
        else:
            print('Product not found')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        session.close()
        
        
# FInding Product by Id
def find_product_by_id():
    id_ = input("Enter the product's id: ")
    product = session.query(Product).filter_by(id=id_).first()
    if product:
         print(f'ID: {product.id}, Name: {product.name}, Category: {product.category}')
    else:
        print('Product not found')
        
        
# Create Product
def create_product():
    name = input("Enter Product's name: ")
    price = input("Enter Product's Price: ")
    category = input("Enter Product's Category: ")
    quantity = input("Enter Product's quantity: ")
    supplier_id = input("Enter supplier's id: ")
    try:
        new_product = Product(name=name, price=price, category=category, quantity=quantity, supplier_id=supplier_id)
        session.add(new_product)
        session.commit()
        print("Product added successfully")
    except Exception as exc:
        print(f"An error occurred: {exc}")