import random
import datetime

class PersonalAssistant:
    def __init__(self):
        self.greetings = ['Hello!', 'Hi there!', 'Greetings!', 'Nice to see you!']
        self.commands = {
            'time': self.get_current_time,
            'date': self.get_current_date,
            'quote': self.get_random_quote
        }

    def greet_user(self):
        return random.choice(self.greetings)

    def process_command(self, command):
        if command.lower() in self.commands:
            return self.commands[command.lower()]()
        else:
            return "Sorry, I don't understand that command."

    def get_current_time(self):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M')}."

    def get_current_date(self):
        now = datetime.datetime.now()
        return f"Today is {now.strftime('%B %d, %Y')}."

    def get_random_quote(self):
        quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "It does not matter how slowly you go as long as you do not stop. - Confucius"
        ]
        return random.choice(quotes)

def main():
    assistant = PersonalAssistant()
    print(assistant.greet_user())

    while True:
        user_input = input("How can I assist you? (Type 'exit' to quit) ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            response = assistant.process_command(user_input)
            print(response)

if __name__ == "__main__":
    main()
