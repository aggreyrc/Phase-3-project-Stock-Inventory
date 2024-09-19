from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Float, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///stocks.db')
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

# Creating Products Table

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)
    category = Column(String())
    quantity = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    
    supplier = relationship('Supplier', back_populates='products')

    
    
    def __repr__(self):
        return f'Product(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'price={self.price})' + \
            f'category={self.category}, ' + \
            f'quantity={self.quantity}, ' + \
            f'supplier_id={self.supplier_id})'
                
                
# Creating Customer Table

class Customer(Base):
    __tablename__ = 'customers'
    
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    phone = Column(Integer)
    email = Column(String(255))
    address = Column(String(255))

    # Relationship to sales
    sales = relationship('Sale', back_populates='customer')
    
    def __repr__(self):
        return f'Customer(customer_id={self.customer_id}, ' + \
            f'name={self.name}, ' + \
            f'phone={self.phone}' + \
            f'email={self.email}, ' + \
            f'address={self.address})'
                
                
                
# Creating Supplier Table

class Supplier(Base):
    __tablename__ = 'suppliers'
    
    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    phone_number = Column(String(50))
    email = Column(String(255))
    address = Column(String(255))
    
    # Relationship to products
    products = relationship('Product', back_populates='supplier')
    
    
    def __repr__(self):
        return f'Supplier(supplier_id={self.supplier_id}, ' + \
                f'name = {self.name}, ' + \
                f'phone_number = {self.phone_number}, ' + \
                f'email = {self.email}, ' + \
                f'address = {self.address})'
                
# Creating Sale table

class Sale(Base):
    __tablename__ = 'sales'
    
    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    sale_date = Column(DateTime)
    total_amount = Column(Float)

    # Relationship to sale details and customer
    details = relationship('SaleDetail', back_populates='sale')
    customer = relationship('Customer', back_populates='sales')
    
    
    def __repr__(self):
        return f'Sale(sale_id={self.sale_id}, ' + \
                f'customer_id={self.customer_id}, ' + \
                f'sale_date={self.sale_date}, ' + \
                f'total_amount={self.total_amount})'


# Creating SaleDetails table
class SaleDetail(Base):
    __tablename__ = 'sales_details'
    
    sale_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    sale_id = Column(Integer, ForeignKey('sales.sale_id'))
    product_id = Column(Integer)
    quantity = Column(Integer)
    price = Column(Float)

    # Relationship to sales
    sale = relationship('Sale', back_populates='details')
    
    
    def __repr__(self):
        return f'SaleDetail(sale_detail_id={self.sale_detail_id}, ' + \
                f'sale_id={self.sale_id}, ' + \
                f'product_id={self.product_id}, ' + \
                f'quantity={self.quantity}, ' + \
                f'price={self.price})'
                
    

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tables created successfully")
