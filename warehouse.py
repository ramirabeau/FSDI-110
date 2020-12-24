# imports
from menu import print_menu, print_header, clear, print_line, print_product
from homework import calculate_age, calculate_tip
from product import Product


# global vars

catalog = []
next_id = 1

# functions


def register_product():
    # title, category, stock, price
    global next_id

    try:
        print_header("    Register a new product    ")
        title = input("Please provide the Title:  ")
        category = input("Please provide the Category:  ")
        stock = int(input("Please provide the Stock Quantity:  "))
        price = float(input("Please provide the Price:  "))

        # Create an object
        # Upperclase is for the class; lowercase is for the object
        the_product = Product(next_id, title, category, stock, price)
        next_id = next_id + 1

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
        else:
            print('There are no "Out of Stock" items')


def total_value():
    print_header("** Total Stock Value **")
    product_value = 0.00
    for prod in catalog:
        product_value = product_value + ((prod.price) * (prod.stock))
        #print(prod.title + (str(product_value)))
    print("** The total value of the products is:  $" + (str(product_value)))


def cheapest_item():
    print_header("** The Cheapest Item **")

    if (len(catalog) < 1):
        print("** Error, you have an empty catalog. Register a product first. **")
        return

    cheapest = catalog[0]
    for prod in catalog:
        if (float(prod.price < cheapest.price)):
            cheapest = prod
    print_product(cheapest)


"""
1 - show the catalog to the user
2 - ask the euser to choose an id to delete
3 - create flag ( found = False) - IMPLEMENT LATER
4 - travel the list
5 - if the id is equal to the id provided by the user
6 - if it is, then remove the product
7 - set the flag to true - IMPLEMENT LATER
"""


def delete_product():
    print_header("** Delete Product **")
    print_catalog()
    selected = input(
        "Choose the ID number of the product you would like to delete:  ")
    found = False
    for prod in catalog:
        if (str(prod.id) == selected):
            found = True
            catalog.remove(prod)

    if(found):
        print("** Product Removed **")
    else:
        print("** Error, you have selected an invalid selection, try again.")
        return


def update_price():
    print_header("** Update Price **")
    print_catalog()
    selected = input(
        "Choose the ID number of the product you would like to update:  ")
    found = False
    for prod in catalog:
        if (str(prod.id) == selected):
            found = True
            new_price = float(input("Enter the new price:  "))
            prod.price = new_price

    if(found):
        print("** The price has been updated **")
    else:
        print("** Error, you have selected an invalid selection, try again.")
        return


def update_quantity():
    print_header("** Update Stock Quantity **")
    print_catalog()
    selected = input(
        "Choose the ID number of the product you would like to update:  ")
    found = False
    for prod in catalog:
        if (str(prod.id) == selected):
            found = True
            new_stock = int(input("Enter the new stock quantity:  "))
            prod.stock = new_stock

    if(found):
        print("** The stock quantityhas been updated **")
    else:
        print("** Error, you have selected an invalid selection, try again.")
        return

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
    elif (option == "5"):
        cheapest_item()
    elif (option == "6"):
        delete_product()
    elif (option == "7"):
        update_price()
    elif (option == "8"):
        update_quantity()
    elif (option == "a"):
        calculate_age()
    elif(option == "b"):
        calculate_tip()
    elif (option == "x"):
        print("System closing")
    else:
        print("Invalid Option")
    input("Press Enter to continue...")
