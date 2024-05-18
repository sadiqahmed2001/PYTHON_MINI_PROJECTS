import time

def intro():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a mysterious forest.")

def choose_path():
    print("\nWhich path do you choose?")
    print("1. Take the left path.")
    print("2. Take the right path.")
    choice = input("Enter your choice: ")
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Please try again.")
        choose_path()

def left_path():
    print("\nYou chose the left path.")
    print("You encounter a friendly squirrel.")
    print("The squirrel leads you to safety.")
    print("Congratulations! You win!")

def right_path():
    print("\nYou chose the right path.")
    print("You encounter a fierce dragon.")
    print("You try to run away, but the dragon catches you.")
    print("Game over!")

def main():
    intro()
    time.sleep(2)
    choose_path()

if __name__ == '__main__':
    main()
