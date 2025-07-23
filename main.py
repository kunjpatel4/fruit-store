from controller import fruit_manager, customer

def main_menu():
    while True:
        print("\n=== FRUIT STORE ===")
        print("1. Add Fruit")
        print("2. View Fruit Stock")
        print("3. Update Fruit")
        print("4. Buy Fruit (Customer)")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            fruit_manager.add_fruit()
        elif choice == '2':
            fruit_manager.view_fruits()
        elif choice == '3':
            fruit_manager.update_fruit()
        elif choice == '4':
            customer.buy_fruit()
        elif choice == '5':
            print("Thank you for using the Fruit Store App ")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
