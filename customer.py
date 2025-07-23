from controller.fruit_manager import load_fruits, save_fruits
from controller.logger import log_transaction

def buy_fruit():
    fruits = load_fruits()
    if not fruits:
        print("No fruits available.")
        return
    fruit_name = input("Enter fruit to buy: ").strip().capitalize()
    if fruit_name not in fruits:
        print(" Fruit not found.")
        return
    try:
        qty = int(input("Enter quantity to buy: "))
        if qty <= 0 or qty > fruits[fruit_name]['quantity']:
            print(" Invalid quantity.")
            return
        cost = qty * fruits[fruit_name]['price']
        fruits[fruit_name]['quantity'] -= qty
        save_fruits(fruits)
        log_transaction(f"Customer bought {qty} {fruit_name}(s) for ₹{cost}")
        print(f" Bought {qty} {fruit_name}(s) for ₹{cost}")
    except ValueError:
        print(" Enter a valid number.")
