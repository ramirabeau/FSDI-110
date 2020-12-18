# imports
from menu import print_menu, print_header, clear
from homework import calculate_age, calculate_tip


# global vars

# functions


clear()


def register_product():
    # title, category, stock, price
    print_header("    Register a new product    ")
    title = input("Please provide the Title:  ")
    category = input("Please provide the Category:  ")
    stock = input("Please provide the Stock level:  ")
    price = input("Please provide the Price:  ")


# Instructions
option = ""
while(option != "x"):
    print_menu()
    option = input("Please chose an option:  ")
    if (option == "1"):
        register_product()
    elif (option == "2"):
        print("Option 2")
    elif (option == "a"):
        calculate_age()
    elif(option == "b"):
        calculate_tip()
    elif (option == "x"):
        print("System closing")
    else:
        print("Invalid Option")

clear()


# print("You chose: " + option)
