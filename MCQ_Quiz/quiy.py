import json
import random
import os

# File to store quiz questions
QUESTIONS_FILE = 'questions.json'

def load_questions():
    """Load questions from the file."""
    if not os.path.exists(QUESTIONS_FILE):
        return []
    with open(QUESTIONS_FILE, 'r') as file:
        return json.load(file)

def save_questions(questions):
    """Save questions to the file."""
    with open(QUESTIONS_FILE, 'w') as file:
        json.dump(questions, file, indent=4)

def add_question(questions):
    """Add a new question."""
    question = input("Enter the question: ")
    options = []
    for i in range(4):
        option = input(f"Enter option {i + 1}: ")
        options.append(option)
    correct_option = input("Enter the correct option number (1-4): ")
    questions.append({
        'question': question,
        'options': options,
        'correct_option': int(correct_option)
    })
    save_questions(questions)
    print("Question added.")

def take_quiz(questions):
    """Take the quiz."""
    if not questions:
        print("No questions available.")
        return

    random.shuffle(questions)
    score = 0

    for question in questions:
        print(f"\n{question['question']}")
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")
        answer = input("Enter the correct option number: ")
        if int(answer) == question['correct_option']:
            score += 1
            print("Correct!")
        else:
            print("Incorrect.")

    print(f"\nYour score: {score}/{len(questions)}")

def main():
    questions = load_questions()
    while True:
        print("\nQuiz Application")
        print("1. Add Question")
        print("2. Take Quiz")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_question(questions)
        elif choice == '2':
            take_quiz(questions)
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == '__main__':
    main()
