import sqlite3

class Product:
    def __init__(self,name,category,price,stock,expiration_date):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.expiration_date = expiration_date

    def __str__(self):
        return f"Product Name: {self.name}\nCategory of the Product: {self.category}\nPrice of the Product: {self.price}\nStock Number of the Product: {self.stock}\nExpiration Date of the Product: {self.expiration_date}"
    def __len__(self):
        return self.stock

class SuperMarket:
    def __init__(self):
        self.create_connect()

    def create_connect(self):
        self.connect = sqlite3.connect("supermarket.db")

        self.cursor = self.connect.cursor()

        query = "CREATE TABLE IF NOT EXISTS products (name TEXT,category TEXT, price FLOAT,stock INT, expiration_date DATE)"

        self.cursor.execute(query)

        self.connect.commit()

    def disconnect(self):
        self.connect.close()

    def show_all_products(self):

        query = "SELECT * FROM products"

        self.cursor.execute(query)

        products = self.cursor.fetchall()
        print("*************************************************")
        if len(products) == 0:
            print("No Product Available!")
        else:
            for i in products:
                print("Product Name: {}\nCategory of the Product: {}\nPrice of the Product: {}\nStock Number of the Product: {}\nExpiration Date of the Product: {}".format(i[0],i[1],i[2],i[3],i[4]))
                print("*************************************************")

    def add_product(self,Product):
        query = "INSERT INTO products VALUES (?,?,?,?,?)"
        query_name_control = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query_name_control, (Product.name,))
        existing_product = self.cursor.fetchall()
        if existing_product:
            print("the Product Already Available")
        else:
            self.cursor.execute(query,(Product.name, Product.category, Product.price, Product.stock, Product.expiration_date))
            print("the Product was added!")
            self.connect.commit()

    def del_product(self,product_name):
        query = "DELETE FROM products WHERE name = ?"
        query_name_control = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query_name_control, (product_name,))
        existing_product = self.cursor.fetchall()
        if not existing_product:
            print("No Product Available!")
        else:
            self.cursor.execute(query, (product_name,))
            print("the Product was deleted!")
            self.connect.commit()

    def update_product(self, product_name):
        query = "UPDATE products set name = ?, category = ?, price = ?, stock = ?, expiration_date = ? WHERE name = ?"
        query_name_control = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query_name_control, (product_name,))
        existing_product = self.cursor.fetchall()
        if not existing_product:
            print("No Product Avaliable")
        else:
            new_product_name = input("New Product Name: ")
            new_product_name = new_product_name.strip().lower()
            new_category = input("New Category: ")
            new_category = new_category.strip().lower()
            new_price = float(input("New Price: "))
            new_stock = int(input("New Stock: "))
            new_expiration_date = input("New Expiration Date (YYYY-MM-DD): ")
            self.cursor.execute(query, (new_product_name, new_category, new_price, new_stock,new_expiration_date, product_name,))
            print("the Product was updated!")
            self.connect.commit()

    def show_entered_product(self, product_name):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (product_name,))
        products = self.cursor.fetchall()

        if not products:
            print("No Product Available!")
        else:
            for i in products:
                print("*************************************************")
                print("Product Name: {}\nCategory of the Product: {}\nPrice of the Product: {}\nStock Number of the Product: {}\nExpiration Date of the Product: {}".format(i[0], i[1], i[2], i[3], i[4]))
                print("*************************************************")

    def increase_stock(self, product_name, number):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (product_name,))
        products = self.cursor.fetchall()

        if not products:
            print("No Product Available!")
        else:
            for i in products:
                stock = i[3]
                number += stock
            print("Current Stock: {}".format(number))

        query_update = "UPDATE products SET stock = ? WHERE name = ?"
        self.cursor.execute(query_update, (number,product_name,))
        self.connect.commit()

    def decrease_stock(self, product_name, number):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (product_name,))
        products = self.cursor.fetchall()

        if not products:
            print("No Product Available!")
        else:
            for i in products:
                stock = i[3]
                new_stock = stock - number
            print("Current Stock: {}".format(new_stock))

            query_update = "UPDATE products SET stock = ? WHERE name = ?"
            self.cursor.execute(query_update, (new_stock, product_name,))
            self.connect.commit()

    def increase_price(self, product_name, amount):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (product_name,))
        products = self.cursor.fetchall()
        if not products:
            print("No Product Available!")
        else:
            for i in products:
                price = i[2]
                amount += price
            print("Current Price: {}".format(amount))

            query_update = "UPDATE products SET price = ? WHERE name = ?"
            self.cursor.execute(query_update, (amount, product_name,))
            self.connect.commit()

    def decrease_price(self, product_name, amount):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (product_name,))
        products = self.cursor.fetchall()
        if not products:
            print("No Product Available!")
        else:
            for i in products:
                price = i[2]
                new_price = price - amount
            print("Current Price: {}".format(new_price))

            query_update = "UPDATE products SET price = ? WHERE name = ?"
            self.cursor.execute(query_update, (new_price, product_name,))
            self.connect.commit()