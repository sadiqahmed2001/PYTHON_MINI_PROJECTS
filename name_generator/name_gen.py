import random

class FantasyNameGenerator:
    def __init__(self, themes):
        self.themes = themes

    def generate_name(self, theme):
        # Sample syllables for demonstration
        syllables = {
            'elven': ['Ae', 'Ar', 'En', 'Gal', 'Li', 'Tha', 'Ver', 'Win'],
            'dwarven': ['Bal', 'Dor', 'Dur', 'Gim', 'Kil', 'Mor', 'Thor', 'Zar'],
            'magical': ['Astra', 'Celest', 'Eldri', 'Lumin', 'Mysti', 'Sylva', 'Vala', 'Zephyr']
        }
        if theme in syllables:
            name = ''.join(random.sample(syllables[theme], random.randint(2, 3)))
            return name.capitalize()
        else:
            return "Unknown theme. Please choose from available themes."

def main():
    print("Welcome to the Fantasy Character Name Generator!")

    # Available themes for character names
    themes = ['elven', 'dwarven', 'magical']

    # Create a FantasyNameGenerator instance
    generator = FantasyNameGenerator(themes)

    # Generate and display a random fantasy character name
    theme = random.choice(themes)
    print(f"Generating a random {theme} character name:")
    print(generator.generate_name(theme))

if __name__ == "__main__":
    main()
