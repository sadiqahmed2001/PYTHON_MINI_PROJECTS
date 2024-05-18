import random

# List of predefined facts
facts = [
    "Honey never spoils. Archaeologists have discovered pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
    "A group of flamingos is called a flamboyance.",
    "The electric chair was invented by a dentist.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "The shortest international flight in the world lasts only 8 minutes. It connects the two Caribbean islands of Saint Kitts and Nevis.",
    "Cows have best friends and they tend to spend most of their time together.",
    "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the iron.",
    "Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
    "Bananas are berries, but strawberries are not."
]

def generate_random_fact():
    """Generate a random fact from the list."""
    return random.choice(facts)

def main():
    print("Welcome to the Random Fact Generator!")
    input("Press Enter to get a random fact...")

    # Generate and display a random fact
    fact = generate_random_fact()
    print("\nHere's your random fact:")
    print(fact)

if __name__ == "__main__":
    main()
