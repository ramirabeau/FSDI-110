def print_menu():
    print("*" * 30)
    print("    Welcome to PyWarehouse    ")
    print("*" * 30)

    print("[1] Register Product")
    print("[2] View Catalog")
    print("[a] Calculate age")
    print("[b] Calculate tip (15%)")
    print("[x] Close the system")


def print_header(header_text):
    clear()
    print("-" * 40)
    print(header_text)
    print("-" * 40)


def clear():
    print("\n\n\n\n\n\n")
