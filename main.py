questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest ocean?": "Pacific",
    "What is the currency of Japan?": "Yen",
    "What is the tallest mountain in the world?": "Everest",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for gold?": "Au",
    "What is the hardest natural substance on Earth?": "Diamond",
    "What is the longest river in the world?": "Nile",
    "What is the largest mammal in the world?": "Blue Whale",
    "What is the capital of Australia?": "Canberra",
    "What is the smallest country in the world?": "Vatican City",
    "What is the largest desert in the world?": "Sahara",
    "What is the capital of Brazil?": "Brasília",
    "What is the largest lake in the world?": "Caspian Sea",
    "What is the capital of Canada?": "Ottawa",
    "What is the largest island in the world?": "Greenland",
    "What is the capital of India?": "New Delhi",
    "What is the largest bone in the human body?": "Femur",
    "What is the capital of Germany?": "Berlin"
}

  
  
def play_game():
    score = 0
    i =0
    for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"Your final score is {score}/{len(questions)}")

play_game()






