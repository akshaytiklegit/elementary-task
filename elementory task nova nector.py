class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

def create_character():
    name = input("Enter your character's name: ")
    character_class = input("Choose your character class (e.g., Warrior, Mage, Thief): ")
    return Character(name, character_class)

def display_menu():
    print("\n1. View Inventory")
    print("2. Continue Adventure")
    print("3. Quit")

def main():
    print("Welcome to the Adventure Game!")
    character = create_character()
    print(f"Welcome, {character.name} the {character.character_class}!")

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(f"Inventory: {character.inventory}")
        elif choice == "2":
            adventure(character)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def adventure(character):
    print("You set off on an adventure...")
    print("You come across a fork in the road. Do you go left or right?")
    
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == 'left':
        print("You encounter a wild beast!")
        fight_or_flight(character)
    elif choice == 'right':
        print("You find a treasure chest!")
        character.add_to_inventory("Gold Coin")
    else:
        print("Invalid choice. Returning to main menu.")

def fight_or_flight(character):
    print("Do you fight the beast or run away?")
    choice = input("Enter 'fight' or 'run': ").lower()

    if choice == 'fight':
        print("You bravely fight the beast and win!")
        character.add_to_inventory("Beast Claw")
    elif choice == 'run':
        print("You manage to escape unharmed.")
    else:
        print("Invalid choice. Returning to main menu.")

if __name__ == "__main__":
    main()
