# import random

# # List of predefined jokes
# jokes = [
#     "Why don't scientists trust atoms? Because they make up everything!",
#     "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
#     "Parallel lines have so much in common. It’s a shame they’ll never meet.",
#     "I'm reading a book on anti-gravity. It's impossible to put down!",
#     "Why did the scarecrow win an award? Because he was outstanding in his field!",
#     "I told my wife she was drawing her eyebrows too high. She looked surprised.",
#     "Why don't skeletons fight each other? They don't have the guts.",
#     "Why was the math book sad? Because it had too many problems.",
#     "I'm on a whiskey diet. I've lost three days already!",
#     "What do you call fake spaghetti? An impasta!"
# ]

# def generate_random_joke():
#     """Generate a random joke from the list."""
#     return random.choice(jokes)

# def main():
#     print("Welcome to the Random Joke Generator!")
#     input("Press Enter to get a random joke...")

#     # Generate and display a random joke
#     joke = generate_random_joke()
#     print("\nHere's your random joke:")
#     print(joke)

# if __name__ == "__main__":
#     main()


import requests

def fetch_random_joke(category):
    url = f"https://api.jokes.one/jod?category={category}"
    headers = {"content-type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        joke = response.json()['contents']['jokes'][0]['joke']['text']
        return joke
    else:
        return "Failed to fetch joke. Please try again later."

def main():
    print("Welcome to the Random Joke Generator!")
    categories = ["general", "dad-jokes", "programming", "puns"]  # Example joke categories
    while True:
        print("\nSelect a joke category:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category.capitalize()}")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == '0':
            print("Exiting the Random Joke Generator. Goodbye!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(categories):
            selected_category = categories[int(choice) - 1]
            joke = fetch_random_joke(selected_category)
            print("\nHere's a joke for you:")
            print(joke)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
