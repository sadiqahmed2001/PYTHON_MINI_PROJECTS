import wikipedia

def chat():
    print("Hello! I'm your Wikipedia Chatbot.")
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            # Try to find the user's input on Wikipedia
            page = wikipedia.page(user_input)
            print("Wikipedia: ", page.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print("Wikipedia: There are multiple possible options for your query. Please be more specific.")
        except wikipedia.exceptions.PageError as e:
            print("Wikipedia: I couldn't find any information on that. Could you try another topic?")

if __name__ == "__main__":
    chat()
