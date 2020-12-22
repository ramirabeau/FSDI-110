# imports
from menu import print_menu, print_header, clear, print_line, print_product
from homework import calculate_age, calculate_tip
from product import Product


# global vars

catalog = []

# functions


def register_product():
    # title, category, stock, price

    try:
        print_header("    Register a new product    ")
        title = input("Please provide the Title:  ")
        category = input("Please provide the Category:  ")
        stock = int(input("Please provide the Stock level:  "))
        price = float(input("Please provide the Price:  "))

        # Create an object
        # Upperclase is for the class; lowercase is for the object
        the_product = Product(0, title, category, stock, price)

        print(the_product)

        # Add object to a list
        catalog.append(the_product)
        print_line()
        print("** Product Resgistered **")
    except:
        print_line()
        print("** There is an error, verify the values and try again **")


def print_catalog():
    # Travel the list, get the product, display the product
    print_header("** Current Catalog **")
    for prod in catalog:
        print_product(prod)


def stock_level():
    # Display Out of Stock message for the items with zero balance
    print_header("** Product Out of Stock **")

    for prod in catalog:
        if (prod.stock == 0):
            print_product(prod)


def total_value():
    print_header("** Total Stock Value **")
    product_value = 0.00
    for prod in catalog:
        product_value = product_value + ((prod.price) * (prod.stock))
        #print(prod.title + (str(product_value)))
    print(str(product_value))


# Instructions
option = ""

while(option != "x"):
    clear()
    print_menu()
    option = input("Please chose an option:  ")

    if (option == "1"):
        register_product()

    elif (option == "2"):
        print_catalog()
    elif (option == "3"):
        stock_level()
    elif (option == "4"):
        total_value()
    elif (option == "a"):
        calculate_age()
    elif(option == "b"):
        calculate_tip()
    elif (option == "x"):
        print("System closing")
    else:
        print("Invalid Option")
    input("Press Enter to continue...")


# print("You chose: " + option)
