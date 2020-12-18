def calculate_age():
    print("This is the age")


def calculate_tip():

    item_cost = float(input("Please enter the cost of the item:  "))
    tip_amount = (item_cost) * .15
    total_cost = (item_cost + tip_amount)
    print("The amount of the tip is:  " + str(tip_amount))
    print("The total cost is:  " + str(total_cost))
