import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine = CoffeeMaker()
coffee_menu = Menu()
payment = MoneyMachine()


on = True
while on:
    choice = input(f"Welcome to the Coffee Maker!  Choose your beverage: {coffee_menu.get_items()}")
    if choice=="report":
        machine.report()
    elif choice =="off":
        on = False
    else:
        if coffee_menu.find_drink(choice)==None:
            print("Please try again.")
        else:
            drink = coffee_menu.find_drink(choice)
            if machine.is_resource_sufficient(drink):
            #paid = payment.process_coins()
                if payment.make_payment(drink.cost):
                    machine.make_coffee(drink)
            else:
                on = False