from helpers import(
    exit_program,
    list_all_products,
    find_product_by_name,
    find_product_by_id,
    create_product
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
      else:
          print('Invalid choice. Please try again.')
          
          
def menu():
      print('\nWelcome to the Stocks Management System')
      print('0. Exit')
      print('1. List all products')
      print('2. Find product by name') 
      print('3. Find product by ID')
      print('4. Create Product')
      
      
      
if __name__ == "__main__":
    main()
    
