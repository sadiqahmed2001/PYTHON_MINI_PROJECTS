from textgenrnn import textgenrnn 

def generate_poetry(text_data, num_epochs=20):
    """Generate poetry using the provided text data."""
    textgen = textgenrnn.TextgenRnn()
    textgen.train_from_file(text_data, num_epochs=num_epochs)
    generated_poems = textgen.generate(5, return_as_list=True)
    return generated_poems

def main():
    text_data = "path/to/your/text/data.txt"  # Path to your text data file
    generated_poems = generate_poetry(text_data)
    print("Generated Poems:")
    for poem in generated_poems:
        print(poem)

if __name__ == "__main__":
    main()
