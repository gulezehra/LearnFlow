import random

# Question database organized by subject and difficulty level
quiz_content = {
    "mathematics": {
        "simple": [
            {"query": "Calculate 5 + 3?", "options": ["6", "7", "8", "9"], "answer": "8"},
            {"query": "What is 2 multiplied by 2?", "options": ["2", "3", "4", "5"], "answer": "4"},
            {"query": "Find the result of 10 - 4.", "options": ["6", "5", "4", "3"], "answer": "6"},
            {"query": "What is 6 divided by 2?", "options": ["2", "3", "4", "5"], "answer": "3"},
            {"query": "Sum of 3 and 5?", "options": ["7", "8", "9", "10"], "answer": "8"},
        ],
        "intermediate": [
            {"query": "What is 12 divided by 4?", "options": ["1", "2", "3", "4"], "answer": "3"},
            {"query": "What is 3 raised to the power of 2?", "options": ["6", "7", "8", "9"], "answer": "9"},
            {"query": "Calculate 15 - 7.", "options": ["6", "7", "8", "9"], "answer": "8"},
            {"query": "What is 5 times 5?", "options": ["20", "25", "30", "35"], "answer": "25"},
            {"query": "Pi (π) to two decimal places?", "options": ["3.12", "3.14", "3.16", "3.18"], "answer": "3.14"},
        ],
        "challenging": [
            {"query": "What is the square root of 144?", "options": ["10", "11", "12", "13"], "answer": "12"},
            {"query": "Calculate 15 multiplied by 6.", "options": ["75", "80", "85", "90"], "answer": "90"},
            {"query": "Find 7! (7 factorial).", "options": ["5040", "720", "630", "7200"], "answer": "5040"},
            {"query": "What is 2 raised to the power of 10?", "options": ["1024", "512", "256", "128"], "answer": "1024"},
            {"query": "Derivative of x^2?", "options": ["2x", "x^2", "x", "3x"], "answer": "2x"},
        ],
    },
    "biology": {
        "simple": [
            {"query": "Which planet is referred to as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
            {"query": "At what temperature does water boil?", "options": ["90°C", "100°C", "110°C", "120°C"], "answer": "100°C"},
            {"query": "Which gas is essential for human respiration?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
            {"query": "Which part of the plant is responsible for photosynthesis?", "options": ["Roots", "Stem", "Leaves", "Flowers"], "answer": "Leaves"},
            {"query": "Chemical formula for water?", "options": ["CO2", "H2O", "O2", "NaCl"], "answer": "H2O"},
        ],
        "intermediate": [
            {"query": "What is the symbol for gold in chemistry?", "options": ["Ag", "Au", "Pt", "Pb"], "answer": "Au"},
            {"query": "What do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
            {"query": "Largest organ in the human body?", "options": ["Heart", "Liver", "Skin", "Lung"], "answer": "Skin"},
            {"query": "pH level of pure water?", "options": ["6", "7", "8", "9"], "answer": "7"},
            {"query": "What is the powerhouse of a cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"], "answer": "Mitochondria"},
        ],
        "challenging": [
            {"query": "What is the speed of light?", "options": ["3 x 10^8 m/s", "2 x 10^8 m/s", "1 x 10^8 m/s", "4 x 10^8 m/s"], "answer": "3 x 10^8 m/s"},
            {"query": "Most abundant gas in Earth's atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Nitrogen"},
            {"query": "Main function of red blood cells?", "options": ["Carry oxygen", "Fight infections", "Clot blood", "Transport nutrients"], "answer": "Carry oxygen"},
            {"query": "Main gas in fizzy drinks?", "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": "Carbon Dioxide"},
            {"query": "What does 'O' stand for in the periodic table?", "options": ["Gold", "Oxygen", "Osmium", "Oganesson"], "answer": "Oxygen"},
        ],
    },
    "history": {
        "simple": [
            {"query": "Who was the first president of the USA?", "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "answer": "George Washington"},
            {"query": "When did World War I begin?", "options": ["1914", "1918", "1939", "1945"], "answer": "1914"},
            {"query": "Who discovered America?", "options": ["Christopher Columbus", "Ferdinand Magellan", "Marco Polo", "Leif Erikson"], "answer": "Christopher Columbus"},
            {"query": "Which civilization built the pyramids?", "options": ["Greek", "Roman", "Egyptian", "Mayan"], "answer": "Egyptian"},
            {"query": "What year did the Titanic sink?", "options": ["1912", "1905", "1920", "1930"], "answer": "1912"},
        ],
        "intermediate": [
            {"query": "Who authored the Declaration of Independence?", "options": ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"], "answer": "Thomas Jefferson"},
            {"query": "First capital of the USA?", "options": ["New York", "Philadelphia", "Washington D.C.", "Boston"], "answer": "New York"},
            {"query": "Empire ruled by Genghis Khan?", "options": ["Roman", "Mongol", "Ottoman", "British"], "answer": "Mongol"},
            {"query": "Primary cause of the American Civil War?", "options": ["Taxation", "Slavery", "Territorial Expansion", "Trade"], "answer": "Slavery"},
            {"query": "First woman to fly solo across the Atlantic?", "options": ["Amelia Earhart", "Harriet Quimby", "Bessie Coleman", "Nancy Bird"], "answer": "Amelia Earhart"},
        ],
        "challenging": [
            {"query": "Name of the ship that brought the Pilgrims to America?", "options": ["Mayflower", "Santa Maria", "Titanic", "Pinta"], "answer": "Mayflower"},
            {"query": "Year the Berlin Wall fell?", "options": ["1987", "1989", "1990", "1991"], "answer": "1989"},
            {"query": "Who was the Iron Lady?", "options": ["Margaret Thatcher", "Golda Meir", "Angela Merkel", "Indira Gandhi"], "answer": "Margaret Thatcher"},
            {"query": "Motivation behind the Crusades?", "options": ["Trade", "Land", "Religion", "Wealth"], "answer": "Religion"},
            {"query": "Ancient civilization known for pyramids and hieroglyphs?", "options": ["Greek", "Roman", "Egyptian", "Chinese"], "answer": "Egyptian"},
        ],
    },
    "geography": {
        "simple": [
            {"query": "Capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
            {"query": "Which continent is called the 'Dark Continent'?", "options": ["Asia", "Africa", "Australia", "South America"], "answer": "Africa"},
            {"query": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
            {"query": "Longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
            {"query": "Which country has the most natural lakes?", "options": ["Canada", "USA", "Russia", "China"], "answer": "Canada"},
        ],
        "intermediate": [
            {"query": "Which is the smallest continent?", "options": ["Asia", "Australia", "Europe", "Antarctica"], "answer": "Australia"},
            {"query": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"], "answer": "Canberra"},
            {"query": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "Korea", "Thailand"], "answer": "Japan"},
            {"query": "Which country is the largest by land area?", "options": ["Canada", "China", "USA", "Russia"], "answer": "Russia"},
            {"query": "Which river flows through London?", "options": ["Thames", "Seine", "Danube", "Nile"], "answer": "Thames"},
        ],
        "challenging": [
            {"query": "Which country has the most time zones?", "options": ["USA", "Russia", "France", "Australia"], "answer": "France"},
            {"query": "What is the capital of Mongolia?", "options": ["Ulaanbaatar", "Beijing", "Seoul", "Tokyo"], "answer": "Ulaanbaatar"},
            {"query": "Which desert is the largest?", "options": ["Gobi", "Sahara", "Kalahari", "Arabian"], "answer": "Sahara"},
            {"query": "Which two countries share the longest international border?", "options": ["USA & Canada", "Russia & China", "Brazil & Argentina", "India & Pakistan"], "answer": "USA & Canada"},
            {"query": "What is the highest mountain in North America?", "options": ["Mount Rainier", "Mount McKinley", "Mount Elbert", "Mount Hood"], "answer": "Mount McKinley"},
        ],
    },
}

def get_quiz_data(subject, difficulty):
    """Fetch questions based on the selected subject and difficulty."""
    return quiz_content.get(subject, {}).get(difficulty, [])

def display_question(question):
    """Display a single question and its options, and return the user's answer."""
    print(question["query"])
    for idx, option in enumerate(question["options"], start=1):
        print(f"{idx}. {option}")

    while True:
        try:
            choice = int(input("Choose the correct option number: "))
            if 1 <= choice <= len(question["options"]):
                return question["options"][choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(question['options'])}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_quiz():
    """Main function to play the quiz."""
    print("Welcome to the Quiz Game!")
    print("Available subjects: mathematics, biology, history, geography")

    subject = input("Choose a subject from the list above: ").lower()
    while subject not in quiz_content:
        print("Invalid subject. Please choose from the available subjects.")
        subject = input("Choose a subject from the list above: ").lower()

    difficulty = input("Choose a difficulty (simple, intermediate, challenging): ").lower()
    while difficulty not in quiz_content[subject]:
        print("Invalid difficulty. Please choose from simple, intermediate, or challenging.")
        difficulty = input("Choose a difficulty (simple, intermediate, challenging): ").lower()

    questions = get_quiz_data(subject, difficulty)
    if not questions:
        print("No questions available for this subject and difficulty.")
        return

    score = 0
    total_questions = 5  # Set the number of questions to ask
    asked_questions = random.sample(questions, min(len(questions), total_questions))

    for question in asked_questions:
        correct_answer = question["answer"]
        user_answer = display_question(question)
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")

    print(f"Your final score is: {score}/{total_questions}")

if __name__ == "__main__":
    play_quiz()
