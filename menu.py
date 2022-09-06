from prettytable import PrettyTable


class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name: str, water: int, milk: int, coffee: int, cost: float):
        self.name: str = name
        self.cost: float = cost
        self.ingredients: dict = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    menu_table = PrettyTable()

    def __init__(self):
        self.menu: list = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
        self.make_options_table()

    @classmethod
    def get_items(cls):
        """Returns all the names of the available menu items"""
        # options: str = ""
        # for menu_item in self.menu:
        #     options += f"{menu_item.name}/"
        # options: str = '/'.join(menu_item for menu_item in self.menu)

        return cls.menu_table

    def find_drink(self, drink_name: str) -> MenuItem | None:
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for menu_item in self.menu:
            if menu_item.name == drink_name:
                return menu_item
        # If not found, then print the message and return None
        print("Sorry that item is not available.")
        return

    def make_options_table(self):
        self.menu_table.clear()
        self.menu_table.add_column('Coffee', list(map(lambda menu_item: menu_item.__getattribute__('name'), self.menu)))
        self.menu_table.add_column('Cost', list(map(lambda menu_item: menu_item.__getattribute__('cost'), self.menu)))
