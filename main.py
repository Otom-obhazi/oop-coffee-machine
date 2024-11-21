from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


mymoney_machine = MoneyMachine()
coffemaker = CoffeeMaker()
menu = Menu(), MenuItem()

is_on = True


while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? {option}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffemaker.report()
        mymoney_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffemaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
            coffemaker.make_coffee(drink)
