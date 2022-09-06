from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine_ = MoneyMachine()
coffee_menu = Menu()


def print_report():
    """Combines the reports from both coffee machine and moneymaker"""
    coffee_machine.report()
    money_machine_.report()


def run_coffee_machine():
    machine_is_on = True

    while machine_is_on:
        choice: str = input(f"Type 'off' to exit. Type 'report' to get the report.\n​What would you like\n"
                            f"{coffee_menu.get_items()}\n? ")
        if choice == "off":
            return False
        elif choice == "report":
            print_report()
        else:
            drink: MenuItem = coffee_menu.find_drink(choice)
            # If the user typed invalid choice for coffee
            if drink is None:
                # Message is printed while calling the function find_drink
                continue
            # Short circuit principle is applied (i.e. if there is not enough resources
            # you will not proceed with payment)
            elif coffee_machine.is_resource_sufficient(drink) and money_machine_.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)


if __name__ == '__main__':
    pass
