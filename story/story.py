import random

class StoryGenerator:
    def __init__(self):
        self.characters = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        self.settings = ["forest", "castle", "beach", "space", "city"]
        self.conflicts = ["lost treasure", "ancient curse", "forbidden love", "evil wizard", "alien invasion"]
        self.resolutions = ["discover a hidden power", "find true love", "uncover a secret", "save the world", "achieve inner peace"]

    def generate_story(self):
        character = random.choice(self.characters)
        setting = random.choice(self.settings)
        conflict = random.choice(self.conflicts)
        resolution = random.choice(self.resolutions)

        story = f"Once upon a time, {character} found themselves in a {setting}. They encountered {conflict}, but in the end, they {resolution}."
        return story

def main():
    print("Welcome to the Random Story Generator!")

    generator = StoryGenerator()

    print("\nGenerating a random story:")
    story = generator.generate_story()
    print(story)

if __name__ == "__main__":
    main()
