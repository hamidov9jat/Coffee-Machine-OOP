from menu import MenuItem


class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources: dict = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # No need for flag
        # can_make = True
        for ingredient in drink.ingredients:
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, drink: MenuItem):
        """Deducts the required ingredients from the resources."""
        for ingredient in drink.ingredients:
            self.resources[ingredient] -= drink.ingredients[ingredient]
        print(f"Here is your {drink.name} ☕️. Enjoy!")
