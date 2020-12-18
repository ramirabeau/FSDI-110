import datetime


def calculate_age():
    birth_year = int(input("Enter the year you were born (Ex. 2001):  "))
    today_date = datetime.date.today().year
    age = (today_date - birth_year)
    print("You are " + str(age) + " years old.")


def calculate_tip():

    item_cost = float(input("Please enter the cost of the item:  "))
    tip_amount = (item_cost) * .15
    total_cost = (item_cost + tip_amount)
    print(f"The amount of the tip is:  {tip_amount:.02f} ")
    print(f"The total cost is:  {total_cost:.02f} ")
