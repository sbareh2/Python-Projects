from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


mymoneymachine = MoneyMachine()
mycoffeemachine = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? ({options}): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        mycoffeemachine.report()
        mymoneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if mycoffeemachine.is_resource_sufficient(drink):
            if mymoneymachine.make_payment(drink.cost):
                mycoffeemachine.make_coffee(drink)


#choice = input(f'mymachine.get_items()


