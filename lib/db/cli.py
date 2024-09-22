from helpers import(
    exit_program,
    list_all_products,
    find_product_by_name,
    find_product_by_id,
    create_product,
    update_product,
    delete_product
)
from customers import(
  list_all_customers,
  find_customer_by_name,
  find_customer_by_id,
  create_customer,
  update_customer,
  delete_customer
)
from suppliers import(
  list_all_suppliers,
  find_supplier_by_name,
  find_supplier_by_id,
  create_supplier,
  update_supplier,
  delete_supplier
)

def main():
    while True:
      menu()
      choice = input('Enter your choice: ')
      if choice == '0':
        exit_program()
      elif choice == '1':
        list_all_products()
      elif choice == '2':
        find_product_by_name()
      elif choice == '3':
        find_product_by_id()
      elif choice == '4':
        create_product()
      elif choice == '5':
        update_product()
      elif choice == '6':
        delete_product()
      elif choice == '7':
        list_all_customers()
      elif choice == '8':
        find_customer_by_name()
      elif choice == '9':
        find_customer_by_id()
      elif choice == '10':
        create_customer()
      elif choice == '11':
        update_customer()
      elif choice == '12':
        delete_customer()
      elif choice == '13':
        list_all_suppliers()
      elif choice == '14':
        find_supplier_by_name()
      elif choice == '15':
        find_supplier_by_id()
      elif choice == '16':
        create_supplier()
      elif choice == '17':
        update_supplier()
      elif choice == '18':
        delete_supplier()
      else:
          print('Invalid choice. Please try again.')
          
          
def menu():
      print('\nWelcome to the Stocks Management System')
      print('0. Exit')
      print('1. List all products')
      print('2. Find product by name') 
      print('3. Find product by ID')
      print('4. Create Product')
      print('5. Update product price')
      print('6. Delete product')
      print('7. List all customers')
      print('8. Find customer by name')
      print('9. Find customer by ID')
      print('10. Create Customer')
      print('11. Update customer address')
      print('12. Delete customer')
      print('13. List all suppliers')
      print('14. Find supplier by name')
      print('15. Find supplier by ID')
      print('16. Create Supplier')
      print('17. Update supplier phone')
      print('18. Delete supplier')
      
      
      
if __name__ == "__main__":
    main()
    
