from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

end_machine = False
menu = Menu()
resource = CoffeeMaker()
money = MoneyMachine()


while not end_machine:
    option = menu.get_items()
    choice = input(f"What would you like? {option}: ").lower()
    if choice == "off":
        end_machine = True

    elif choice == "report":
        resource.report()
        money.report()

    else:

        drink = menu.find_drink(choice)
        if resource.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            resource.make_coffee(drink)

