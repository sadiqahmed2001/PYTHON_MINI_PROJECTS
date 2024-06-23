from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new ChatBot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

def main():
    print("Welcome to MyChatBot!")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Bot:", response)

if __name__ == '__main__':
    main()
                     
