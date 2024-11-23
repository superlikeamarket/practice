import restaurant_ordering_system as ros

# Test code for the restaurant ordering system

# 1. Create a restaurant
restaurant = ros.Restaurant("The Grand Dine", "123 Food Street", "123-456-7890", 0.0)

# 2. Create some ingredients
ingredient1 = ros.Ingredient("Tomato", 50, 0.5)
ingredient2 = ros.Ingredient("Cheese", 30, 1.0)
ingredient3 = ros.Ingredient("Bread", 20, 0.75)

# 3. Add ingredients to the restaurant warehouse
restaurant.add_ingredient_to_inventory(ingredient1)
restaurant.add_ingredient_to_inventory(ingredient2)
restaurant.add_ingredient_to_inventory(ingredient3)

# 4. Create menu items (dishes)
dish1 = ros.MenuItem("Cheese Sandwich", "A simple cheese sandwich", 5.0, 10)
dish1.add_ingredient_to_recipe(ingredient2, 2)  # 2 units of Cheese
dish1.add_ingredient_to_recipe(ingredient3, 2)  # 2 units of Bread

dish2 = ros.MenuItem("Tomato Soup", "Fresh tomato soup", 4.5, 15)
dish2.add_ingredient_to_recipe(ingredient1, 3)  # 3 units of Tomato

# 5. Add dishes to the restaurant menu
restaurant.add_dish_to_menu(dish1)
restaurant.add_dish_to_menu(dish2)

# 6. Display the restaurant's menu
print("\n--- Restaurant Menu ---")
restaurant.display_menu()

# 7. Create an order
order1 = ros.Order(number=1, table_number=5, total=0, tax=10, tip=5, paid=0, change=0, restaurant=restaurant)

# 8. Add allergies for a customer
order1.ask_for_allergies("John", "Cheese")

# 9. Order dishes
try:
    order1.order_dish("John", dish1, restaurant)  # John is allergic to cheese
except Exception as e:
    print(e)

try:
    order1.order_dish("John", dish2, restaurant)  # No allergy conflict
except Exception as e:
    print(e)

# 10. Cancel a dish
try:
    order1.cancel_dish("John", dish1, restaurant)
except Exception as e:
    print(e)

# 11. Try to complete the order with insufficient payment
try:
    order1.complete_order(restaurant, paid=5)  # Less than the total
except Exception as e:
    print(e)

# 12. Complete the order with sufficient payment
try:
    order1.complete_order(restaurant, paid=10)  # Exact amount or more
except Exception as e:
    print(e)

# 13. Check final restaurant revenue and orders
print("\n--- Restaurant Info ---")
restaurant.display_info()
