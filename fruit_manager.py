import json
from controller.logger import log_transaction

FRUIT_FILE = 'fruits.json'

def load_fruits():
    try:
        with open(FRUIT_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_fruits(data):
    with open(FRUIT_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_fruit():
    fruits = load_fruits()
    fruit_name = input("Enter fruit name: ").strip().capitalize()
    if fruit_name in fruits:
        print("Fruit already exists. Use update option.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        fruits[fruit_name] = {"quantity": quantity, "price": price}
        save_fruits(fruits)
        log_transaction(f"Added new fruit: {fruit_name}, Qty: {quantity}, Price: {price}")
        print(" Fruit added successfully.")
    except ValueError:
        print(" Invalid input. Try again.")

def view_fruits():
    fruits = load_fruits()
    if not fruits:
        print("No fruit stock available.")
        return
    print("\n--- Fruit Stock ---")
    for fruit, details in fruits.items():
        print(f"{fruit}: Qty = {details['quantity']}, Price = ₹{details['price']}")
    print("--------------------")

def update_fruit():
    fruits = load_fruits()
    fruit_name = input("Enter fruit name to update: ").strip().capitalize()
    if fruit_name not in fruits:
        print(" Fruit not found.")
        return
    try:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        fruits[fruit_name] = {"quantity": quantity, "price": price}
        save_fruits(fruits)
        log_transaction(f"Updated fruit: {fruit_name}, New Qty: {quantity}, New Price: {price}")
        print(" Fruit updated successfully.")
    except ValueError:
        print(" Invalid input. Try again.")
