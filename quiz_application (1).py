# PS No. 4: Quiz Application
# Course: BCA 1st Semester (Section 1A)
# Subject: Programming Fundamentals Using Python (RU-100-05-00058)
# University: Rungta International Skills University
# Name: keerti shukla 
# Erp: 00059
import random

TEST_MODE = True

# Question Bank (10 questions stored as a list of dictionaries)
questions = [
    {
        "question": "Keyword to define a function?",
        "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
        "answer": "B"
    },
    {
        "question": 'len("Hi") = ?',
        "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
        "answer": "B"
    },
    {
        "question": "Mutable type?",
        "options": {"A": "tuple", "B": "str", "C": "list", "D": "int"},
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": {"A": "//", "B": "#", "C": "/*", "D": "$"},
        "answer": "B"
    },
    {
        "question": "Which function displays output?",
        "options": {"A": "input()", "B": "print()", "C": "show()", "D": "display()"},
        "answer": "B"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": {"A": "if", "B": "for", "C": "def", "D": "try"},
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": {"A": "int", "B": "str", "C": "bool", "D": "list"},
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": {"A": "%", "B": "//", "C": "**", "D": "/"},
        "answer": "C"
    },
    {
        "question": "Which keyword is used to import a module?",
        "options": {"A": "include", "B": "import", "C": "module", "D": "load"},
        "answer": "B"
    },
    {
        "question": "Which function returns the largest value?",
        "options": {"A": "min()", "B": "sum()", "C": "max()", "D": "len()"},
        "answer": "C"
    }
]


def run_quiz():
    score = 0
    total = 3

    if TEST_MODE:
        selected_questions = questions[:3]
    else:
        selected_questions = random.sample(questions, total)

    print("\n===== WELCOME TO QUIZ APPLICATION =====")
    print("Total Questions:", total)
    print("Pass Marks: 50%")
    print("---------------------------------------")

    for i, q in enumerate(selected_questions):
        print(f"\nQ{i + 1}: {q['question']}")

        for key, value in q["options"].items():
            print(f"{key}. {value}")

        while True:
            answer = input("Enter your answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid option. Enter A, B, C or D.")

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Q{i + 1} Wrong. Correct answer: {q['answer']}")

    percentage = (score / total) * 100

    print("\n========== QUIZ RESULT ==========")
    print(f"Score: {score}/{total} | Percentage: {percentage:.2f}%")

    if percentage >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")
        correct_list = ", ".join([q["answer"] for q in selected_questions])
        print(f"Correct answers: {correct_list}")

    print("=================================")


if __name__ == "__main__":
    run_quiz()
