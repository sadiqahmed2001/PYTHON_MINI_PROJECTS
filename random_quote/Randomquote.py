import random

# List of predefined quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Keep your face always toward the sunshine - and shadows will fall behind you. - Walt Whitman",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson"
]

def generate_random_quote():
    """Generate a random quote from the list."""
    return random.choice(quotes)

def main():
    print("Welcome to the Random Quote Generator!")
    input("Press Enter to get a random quote...")

    # Generate and display a random quote
    quote = generate_random_quote()
    print("\nHere's your random quote:")
    print(quote)

if __name__ == "__main__":
    main()

