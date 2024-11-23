# python 3.12.3 64 bit

"""
OOP, Task 2: Restaurant Ordering System

A program to simulate a restaurant ordering system. The program does:
Allow customers to place orders for items from a menu.
Calculate the total bill, including tax and tip.
Handle special requests and validate orders against available items.

Focus Areas:
Use classes like Restaurant, MenuItem, and Order.
Implement error handling for invalid orders (e.g., unavailable items).
Optimize calculations for generating the bill.
"""


class Restaurant:
    """
    Represents a basic bank account allowing deposits, withdrawals, and balance checks.

    Attributes:
    - name (str): The name of the restaurant.
    - address (str): The address of the restaurant.
    - contact_number (str): The phone number of the restaurant.
    - revenue (float): How much did the restaurant make today.

    Methods:
    - add_dish(menuitem): Adds the dish to the menu.
    - remove_dish(menuitem): Removes the dish from the menu.
    . . . and so on and so forth. Repeat for every class. I won't do it bc it's 
    too long and not the focus of the task.
    """
    def __init__(self, name, address, contact_number, revenue):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.revenue = revenue # Daily revenue.
        self.menu = {} # Key - a dish, value - ingredients.
        self.menu_allergens = {} # Key - a dish, value - allergenic ingredients.
        self.warehouse = {} # Key - ingredient's name, value - its available quantity.
        self.current_orders = [] # Identification numbers of current orders.
        self.completed_orders = [] # Identification numbers of completed orders.
        self.all_orders = [] # Identification numbers of all orders.

    def add_dish_to_menu(self, menuitem):
        """
        Adds the dish to the menu.

        :param menuitem: MenuItem class object to add to the menu (Class object).
        
        the same for every method 
        """
        if menuitem.name not in self.menu:
            # Set the name of the dish as the key and the ingredients' list as the value.
            self.menu[menuitem.name] = menuitem
            print(f"Dish '{menuitem.name}' added to the menu.")
            if menuitem.allergens:
                # Add the dish to the allergen dict along with the specific allergens.
                self.menu_allergens[menuitem.name] = menuitem.allergens
                print(f"It contains the following allergens: {', '.join(menuitem.allergens)}.")
        else:
            print(f"Dish '{menuitem.name}' is already on the menu.")
    
    def remove_dish_from_menu(self, menuitem):
        """Removes the dish from the menu."""
        if menuitem.name in self.menu:
            self.menu.pop(menuitem.name)
            self.menu_allergens.pop(menuitem.name)
            print(f"Dish '{menuitem.name}' removed from the menu.")
        else:
            print(f"Dish '{menuitem.name}' is already not on the menu.")

    def add_ingredient_to_inventory(self, ingredient):
        """Adds the ingredient to the inventory list."""
        if ingredient.name not in self.warehouse:
            # Key - ingredient's name, value - its available quantity.
            self.warehouse[ingredient.name] = ingredient.quantity
            print(f"Ingredient '{ingredient.name}' added to the inventory.")
        else:
            print(f"Ingredient '{ingredient.name}' is already in the inventory.")

    def remove_ingredient_from_inventory(self, ingredient):
        """Removes the ingredient from the inventory list."""
        if ingredient.name in self.warehouse:
            self.warehouse.pop(ingredient.name)
            print(f"Ingredient '{ingredient.name}' removed from the inventory.")
        else:
            print(f"Ingredient '{ingredient.name}' is already not in the inventory.")

    def update_ingredient_quantity_in_warehouse(self, ingredient):
        """Syncs the amount of an ingredient on the inventory list and in reality."""
        self.warehouse[ingredient.name] = ingredient.quantity
        
    def display_info(self):
        """Shows the main info about the restaurant."""
        print(f"""The restaurant '{self.name}', located on {self.address} 
              (contact_number: {self.contact_number}) has made ${self.revenue} today.""")
        
    def display_menu(self):
        """Shows the menu."""
        for dish_name, menuitem in self.menu.items():
            print(f"Dish: {menuitem.name}")
            print(f"Ingredients: {', '.join(menuitem.composition.keys())}")
            print(f"Price: ${menuitem.price}")
            print(f"Description: {menuitem.description}\n")
        

class MenuItem:
    def __init__(self, name, description, price, cooking_time):
        self.name = name 
        self.description = description
        self.price = price # Selling price.
        self.cooking_time = cooking_time # Approximate.
        self.composition = {} # Key - ingredient, value - quantity in the dish.
        self.allergens = {} # Key - allergen type, value - ingredient(s).

    def add_ingredient_to_recipe(self, ingredient, quantity):
        """Adds the ingredient to the recipe."""
        if ingredient.name not in self.composition:
            self.composition[ingredient.name] = quantity
            if ingredient.allergen:
                # Add the allergen to the allergen list.
                if ingredient.allergen not in self.allergens:
                    self.allergens[ingredient.allergen] = []  # Initialize a list for this allergen type.
                self.allergens[ingredient.allergen].append(ingredient.name)
        else:
            # Add amount of an already known ingredient.
            self.composition[ingredient.name] += quantity
        print(f"{quantity} units of Ingredient '{ingredient.name}' added to the recipe.")

    def remove_ingredient_from_recipe(self, ingredient, quantity):
        """Removes the ingredient from the recipe."""
        if ingredient.allergen:
            for allergen_type, allerg_ingr_list in self.allergens.items():
                if ingredient.name in allerg_ingr_list:
                    # Remove the ingredient from the allergen list.
                    allerg_ingr_list.remove(ingredient.name)
                    if not allerg_ingr_list:
                        # Remove the allergen type if the ingredient was the only one of that type.
                        del self.allergens[allergen_type]
            print(f"Ingredient '{ingredient.name}' removed from the recipe.")
        else:
            print(f"Ingredient '{ingredient.name}' is already not in the recipe.")


class Ingredient:
    def __init__(self, name, quantity, price, allergen=None):
        self.name = name
        self.quantity = quantity # How many units are left in the warehouse.
        self.price = price # Buying price.
        self.allergen = allergen # Is it an allergen? What category (Dairy, nut, etc.)?

    def change_quantity(self, restaurant, bought=0, used=0):
        """Updates the quantity of the ingredient."""
        if bought > 0:
            self.buy(bought, restaurant)
        self.quantity += bought - used
        restaurant.update_ingredient_quantity_in_warehouse(self)

    def buy(self, amount, restaurant):
        """Pays for more ingredients out of restaurant's revenue."""
        restaurant.revenue -= amount * self.price
        

class Order:
    def __init__(self, number, table_number, total, tax, tip, paid, change, restaurant):
        # Order number. Use the max function so that every new order will have a 
        # number that is 1 bigger than the last order.
        self.number = max(restaurant.all_orders, default=0) + 1
        # Add the order number to the current order list when initiated.
        restaurant.current_orders.append(self.number)
        restaurant.all_orders.append(self.number)
        self.table_number = table_number
        self.total = total # Total bill.
        self.tax = tax # Mandatory tax, in %.
        self.tip = tip # Tip chosen by the customer, in %.
        self.paid = paid # Money given by the customer.
        self.change = change # Change owed by the restaurant.
        self.customers_dishes = {} # Key - customer's name, value - ordered dishes.
        self.customers_allergies = {} # Key - customer's name, value - allergies.

    def ask_for_allergies(self, customer_name, allergies):
        if customer_name not in self.customers_allergies:
            self.customers_allergies[customer_name] = [] # Initialize a list for this customer.
        self.customers_allergies[customer_name].append(allergies)

    def order_dish(self, customer_name, menuitem, restaurant):
        # Check if the dish is on the menu.
        if menuitem.name not in restaurant.menu:
            raise NonExistingDishError(f"Error: The dish {menuitem.name} is not found in the menu.")
        
        # Check if the tip makes sense.
        if self.tip < 0:
            raise NegativeTipError("Error: You left a negative tip.")
        
        # Create a temporary copy of the dish's composition for this order
        customer_dish_composition = menuitem.composition.copy()

        # Handle allergies and modify the temporary composition if necessary
        for allergy in self.customers_allergies.get(customer_name, []):
            if allergy in menuitem.allergens:
                customer_dish_composition.pop(allergy, None)  # Remove allergen from the copy

        # Check ingredient availability in the restaurant warehouse.
        for ingredient, quantity_needed in customer_dish_composition.items():
            if restaurant.warehouse.get(ingredient, 0) < quantity_needed:
                raise NotEnoughIngredientError(f"Error: Not enough {ingredient} in the warehouse.")

        # Update ingredient quantities.
        for ingredient, quantity_needed in customer_dish_composition.items():
            restaurant.warehouse[ingredient] -= quantity_needed

        # Initialize a list for this customer.
        if customer_name not in self.customers_dishes:
            self.customers_dishes[customer_name] = []
        
        # Add the dish to the order.
        self.customers_dishes[customer_name].append(menuitem.name)
        print(f"'{menuitem.name}' is added to your order, {customer_name}.")

        # Add the price of the dish to the total bill.
        self.total += menuitem.price * ((1 + self.tax / 100) + self.tip / 100)

        
    def cancel_dish(self, customer_name, menuitem, restaurant):
        """Removes the dish from the order."""
        if customer_name not in self.customers_dishes:
            raise DishNotInOrderError(f"{customer_name} hasn't ordered anything yet.")
        if menuitem.name not in restaurant.menu:
            raise NonExistingDishError(f"Error: The dish '{menuitem.name}' is not found in the menu.")
        if menuitem.name not in self.customers_dishes[customer_name]:
            raise DishNotInOrderError(f"'{menuitem.name}' wasn't even ordered.")
        # Remove the dish from the customer's order.
        self.customers_dishes[customer_name].remove(menuitem.name)

    
    def complete_order(self, restaurant, paid=0):
        """Takes in payment. Marks the order as completed."""
        # Check if the payment is enough and calculate the owed change.
        if paid < self.total:
            raise PaidLessThanBillError(f"Error: The bill is {self.total}, you paid less.")
        elif paid == self.total:
            self.change = 0
        else:
            self.change = paid - self.total
            print(f"Change: ${self.change:.2f}")

        # Update revenue.
        restaurant.revenue += self.total

        # Compleeeteeeee!!!!
        restaurant.current_orders.remove(self.number)
        restaurant.completed_orders.append(self.number)
        print(f"Order {self.number} completed.")


"""Error block."""
class NonExistingDishError(Exception):
    """Raised when a dish that's not in the menu is ordered."""
    pass

class DishNotInOrderError(Exception):
    """Raised when a dish that is already not in the order, is tried to be removed from the order."""

class NotEnoughIngredientError(Exception):
    """Raised when there is not enough ingredients for this dish in the warehouse."""
    pass

class NegativeTipError(Exception):
    """Raised when the tip is set to a negative value."""
    pass

class PaidLessThanBillError(Exception):
    """Raised when the client pays less than the total of the order."""
    pass