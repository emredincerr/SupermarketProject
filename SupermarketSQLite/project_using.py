from project import *
import time
from datetime import datetime

print("""
*************************************
Welcome to SuperMarket Project!

Options:

1. Show All Products
2. Show Entered Product
3. Add Product
4. Delete Product
5. Update Product
6. Increase Stock Level
7. Decrease Stock Level
8. Increase Price
9. Decrease Price

Press "q" to exit the program!
*************************************
""")


supermarket = SuperMarket()


while True:
    option = input("Please choose an option...:")

    if option == "q":
        time.sleep(1)
        print("the Program has ended!")
        print("See You Again!")
        break

    elif option == "1":
        time.sleep(1)
        supermarket.show_all_products()

    elif option == "2":
        name = input("Product Name: ")
        name = name.strip().lower()
        time.sleep(1)
        supermarket.show_entered_product(name)

    elif option == "3":
        name = input("Product Name: ")
        name = name.strip().lower()
        category = input("Category of the Product: ")
        category = category.strip().lower()
        price = float(input("Price of the Product: "))
        stock = int(input("Stock Number of the Product: "))
        expiration_date_str = input("Expiration Date of the Product: ")

        expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d").date()
        time.sleep(1)
        supermarket.add_product(Product(name,category,price,stock,expiration_date))

    elif option == "4":
        name = input("Product Name: ")
        name = name.strip().lower()
        time.sleep(1)
        supermarket.del_product(name)

    elif option == "5":
        name = input("the Name of the Product You Want to Change: ")
        name = name.strip().lower()
        time.sleep(2)
        supermarket.update_product(name)

    elif option == "6":
        name = input("Product Name: ")
        name = name.strip().lower()
        number = int(input("Amount of Increase: "))
        time.sleep(1)
        supermarket.increase_stock(name,number)

    elif option == "7":
        name = input("Product Name: ")
        name = name.strip().lower()
        number = int(input("Amount of Decrease: "))
        time.sleep(1)
        supermarket.decrease_stock(name, number)

    elif option == "8":
        name = input("Product Name: ")
        name = name.strip().lower()
        amount = float(input("Amount of Increase: "))
        time.sleep(1)
        supermarket.increase_price(name, amount)

    elif option == "9":
        name = input("Product Name: ")
        name = name.strip().lower()
        amount = float(input("Amount of Decrease: "))
        time.sleep(1)
        supermarket.decrease_price(name, amount)

    else:
        print("There is No Such Option!")
        print("Please, Try Again")




