from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
start = True

while start:
    choice = input("\nWhat would you like to order: " + menu.get_items() + " (type stop if you don't want anything): ")
    if choice == "report":
        coffe_maker.report()
        money_machine.report()
    elif choice == "stop":
        start = False
    else:
        ordered_drink = menu.find_drink(choice)
        if ordered_drink:
            if coffe_maker.is_resource_sufficient(ordered_drink):
                if money_machine.make_payment(ordered_drink.cost):
                    coffe_maker.make_coffee(ordered_drink)
