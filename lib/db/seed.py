from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from models import Customer, Supplier, Product, Sale, SaleDetail, Base  

engine = create_engine('sqlite:///stocks.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Faker
faker = Faker()

# Seed Suppliers
def seed_suppliers(n=10):
    suppliers = []
    for _ in range(n):
        supplier = Supplier(
            name=faker.company(),
            phone_number=faker.phone_number(),
            email=faker.email(),
            address=faker.address()
        )
        suppliers.append(supplier)
        session.add(supplier)
    session.commit()
    return suppliers

# Seed Customers
def seed_customers(n=50):
    customers = []
    for _ in range(n):
        customer = Customer(
            name=faker.name(),
            phone=faker.phone_number(),
            email=faker.email(),
            address=faker.address()
        )
        customers.append(customer)
        session.add(customer)
    session.commit()
    return customers

# Seed Products
def seed_products(suppliers, n=100):
    categories = ['Electronics', 'Furniture', 'Clothing', 'Books', 'Groceries']
    products = []
    for _ in range(n):
        product = Product(
            name=faker.word(),
            price=random.randint(10, 500),
            category=random.choice(categories),
            quantity=random.randint(1, 100),
            supplier_id=random.choice(suppliers).supplier_id
        )
        products.append(product)
        session.add(product)
    session.commit()
    return products

# Seed Sales
def seed_sales(customers, products, n=100):
    sales = []
    for _ in range(n):
        sale = Sale(
            customer_id=random.choice(customers).customer_id,
            total_amount=0.0  # This will be updated after SaleDetails
        )
        session.add(sale)
        session.commit()  # Commit to get sale_id

        # Add SaleDetails for this sale
        total_amount = 0
        for _ in range(random.randint(1, 5)):  # 1 to 5 items per sale
            product = random.choice(products)
            quantity = random.randint(1, 5)
            price = product.price
            sale_detail = SaleDetail(
                sale_id=sale.sale_id,
                product_id=product.id,
                quantity=quantity,
                price=price
            )
            total_amount += price * quantity
            session.add(sale_detail)
        
        # Update total_amount in Sale
        sale.total_amount = total_amount
        sales.append(sale)
        session.commit()

    return sales

# Run the seeding
def main():
    print("Seeding suppliers...")
    suppliers = seed_suppliers()

    print("Seeding customers...")
    customers = seed_customers()

    print("Seeding products...")
    products = seed_products(suppliers)

    print("Seeding sales...")
    seed_sales(customers, products)

    print("Seeding completed!")

if __name__ == '__main__':
    # Create tables if they don't exist
    Base.metadata.create_all(engine)
    
    # Seed the data
    main()
