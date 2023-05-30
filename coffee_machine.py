import money as money

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
cash = 0


def resource_check(ingredients):
    for stuff in ingredients:
        if ingredients[stuff] > resources[stuff]:
            print(f"Sorry, there is not enough {stuff}")
            return False
        else:
            return True

def print_report():
    print(f"Water: {resources['water']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Milk: {resources['milk']} ml")
    print(f"Money: ${cash}")

def make_coffee(ingredients):
    for stuff in ingredients:
        resources[stuff] -= ingredients[stuff]

def enough_money(total, cost):
    if total >= cost:
        change = round((total - cost), 2)
        print(f"Your change is: ${change}")
        global cash
        cash += cost
        return True
    else:
        print("I'm sorry, that's not enough money.  Money refunded")
        return False


turnon = True

while turnon:
    choice = input(f"Welcome to coffee machine.  What would you like? espresso: ${MENU['espresso']['cost']}, latte: ${MENU['latte']['cost']} or cappuccino: ${MENU['cappuccino']['cost']}?")
    if choice =="off":
        turnon=False
    elif choice=="report":
        print_report()
    else:
        chosen = MENU[choice]
        enough = resource_check(chosen['ingredients'])

        if enough:
            print("Please enter your coins \n")
            quarters = float(input("Quarters: ")) * .25
            dimes = float(input("dimes: "))* .1
            nickles = float(input("nickels: "))* 0.5
            pennies = float(input("pennies: "))* 0.01
            total = quarters+dimes+nickles+pennies
            #print(total)
            #enough_money(total, chosen['cost'])
            if enough_money(total,chosen['cost']):
                make_coffee(chosen['ingredients'])
                print(f"Here is your {choice}.  Enjoy!")
        else:
            turnon = False

    #print(MENU[choice]['ingredients']['water'])
    #print(resources['water'])
# check choice against resources
    #print(MENU[choice]['ingredients'])
