import random

# Quiz questions and answers
questions = {
    "What is the capital of France?": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
    "Who wrote 'Romeo and Juliet'?": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
    "What is the largest planet in our solar system?": ["A. Jupiter", "B. Saturn", "C. Mars", "D. Earth"],
    "What is the chemical symbol for water?": ["A. H2O", "B. CO2", "C. O2", "D. HCl"],
    "What is the tallest mammal on Earth?": ["A. Giraffe", "B. Elephant", "C. Lion", "D. Hippopotamus"]
}

# Correct answers
answers = {
    "What is the capital of France?": "A",
    "Who wrote 'Romeo and Juliet'?": "A",
    "What is the largest planet in our solar system?": "A",
    "What is the chemical symbol for water?": "A",
    "What is the tallest mammal on Earth?": "A"
}

def display_question(question, options):
    """Display the question and options to the user."""
    print(question)
    for option in options:
        print(option)

def get_user_answer():
    """Get the user's answer to the question."""
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    while user_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter A, B, C, or D.")
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
    return user_answer

def check_answer(question, user_answer):
    """Check if the user's answer is correct."""
    correct_answer = answers[question]
    return user_answer == correct_answer

def main():
    print("Welcome to the Simple Quiz Game!\n")

    # Shuffle the questions
    shuffled_questions = list(questions.keys())
    random.shuffle(shuffled_questions)

    # Initialize score
    score = 0

    # Iterate through each question
    for question in shuffled_questions:
        display_question(question, questions[question])
        user_answer = get_user_answer()
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    # Display final score
    print("\nYour final score is:", score, "/", len(questions))

if __name__ == "__main__":
    main()
