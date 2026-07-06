QUESTIONS = [
    {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": 1, "money": 100},
    {"q": "What is the capital of France?", "options": ["Berlin", "London", "Paris", "Madrid"], "answer": 2, "money": 200},
    {"q": "Which element has the chemical symbol O?", "options": ["Gold", "Oxygen", "Silver", "Iron"], "answer": 1, "money": 500},
    {"q": "Who wrote 'Romeo and Juliet'?", "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], "answer": 2, "money": 1000},
    {"q": "What is 8 * 7?", "options": ["54", "56", "58", "64"], "answer": 1, "money": 2000},
    {"q": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": 3, "money": 4000},
    {"q": "Which language is primarily used for Android app development?", "options": ["Swift", "Kotlin", "Ruby", "Go"], "answer": 1, "money": 8000},
    {"q": "Which year did the first man land on the moon?", "options": ["1965", "1969", "1972", "1959"], "answer": 1, "money": 16000},
    {"q": "What is the chemical formula for water?", "options": ["CO2", "H2O", "O2", "NaCl"], "answer": 1, "money": 32000},
    {"q": "Which country is home to the Great Barrier Reef?", "options": ["Australia", "USA", "South Africa", "India"], "answer": 0, "money": 64000},
]
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"Your final score is {score}/{len(questions)}")

play_game()






