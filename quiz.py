# Simple Quiz Application

def run_quiz():
    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
            "answer": "C"
        },
        {
            "question": "What is the boiling point of water?",
            "options": ["A) 100°C", "B) 90°C", "C) 80°C", "D) 110°C"],
            "answer": "A"
        }
    ]
    
    score = 0
    
    print("Welcome to the Quiz!")
    
    # Loop through each question
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        
        # Get user's answer
        user_answer = input("Your answer (A/B/C/D): ").upper()
        
        # Check if the answer is correct
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    
    # Print final score
    print(f"\nYour final score is {score}/{len(questions)}")
    
if __name__ == "__main__":
    run_quiz()
