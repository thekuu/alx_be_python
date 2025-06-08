shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")    
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to your list.")
            else:
                print("You didn't enter an item!")
            pass
        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            if item not in shopping_list:
                print("The item is not found in the shopping list!")
            else:
                shopping_list.remove(item)
            pass
        elif choice == "3":
            print("Current list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
            pass
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()