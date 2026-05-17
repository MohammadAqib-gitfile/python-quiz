# Quiz Master Game
# Libraries Used
import random
import time

print("========== QUIZ MASTER ==========")

name = input("Enter Your Name: ")

questions = [
    {
        "question": "Which language is used for AI and Data Science?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. C"],
        "answer": "A"
    },

    {
        "question": "Who is known as the father of computers?",
        "options": ["A. Newton", "B. Charles Babbage", "C. Einstein", "D. Alan Turing"],
        "answer": "B"
    },

    {
        "question": "Which data structure works on FIFO?",
        "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
        "answer": "B"
    },

    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C"
    },

    {
        "question": "Which operator is used for multiplication in Python?",
        "options": ["A. x", "B. *", "C. %", "D. /"],
        "answer": "B"
    },

    {
        "question": "Which function is used to take input from the user?",
        "options": ["A. print()", "B. input()", "C. read()", "D. get()"],
        "answer": "B"
    },

    {
        "question": "Which loop is used when the number of iterations is known?",
        "options": ["A. while", "B. do-while", "C. for", "D. infinite"],
        "answer": "C"
    },

    {
        "question": "Which data type stores True or False values?",
        "options": ["A. int", "B. string", "C. bool", "D. float"],
        "answer": "C"
    },

    {
        "question": "Which keyword is used for conditions in Python?",
        "options": ["A. if", "B. for", "C. loop", "D. switch"],
        "answer": "A"
    },

    {
        "question": "Which collection type is ordered and changeable?",
        "options": ["A. Set", "B. Tuple", "C. List", "D. Dictionary"],
        "answer": "C"
    },

    {
        "question": "What is the extension of a Python file?",
        "options": ["A. .java", "B. .py", "C. .html", "D. .cpp"],
        "answer": "B"
    },

    {
        "question": "Which function displays output on the screen?",
        "options": ["A. print()", "B. output()", "C. show()", "D. display()"],
        "answer": "A"
    },

    {
        "question": "Which module is used to generate random numbers?",
        "options": ["A. math", "B. random", "C. time", "D. os"],
        "answer": "B"
    },

    {
        "question": "Which keyword is used to stop a loop?",
        "options": ["A. continue", "B. pass", "C. break", "D. stop"],
        "answer": "C"
    }
]

random.shuffle(questions)

score = 0

for i, q in enumerate(questions, start=1):

    print(f"\n========== Question {i} ==========")

    print(q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter Your Answer (A/B/C/D): ").upper()

    print("Checking Answer...")
    time.sleep(1)

    if answer == q["answer"]:
        print("Correct Answer!")
        score += 10

    else:
        print("Wrong Answer!")
        print("Correct Answer is:", q["answer"])

# Final Result
print("\n========== FINAL RESULT ==========")

print("Player Name:", name)
print("Your Score:", score, "/", len(questions) * 10)

if score >= 120:
    print("Excellent Performance!")

elif score >= 70:
    print("Good Job!")

else:
    print("Keep Practicing!")

print("Thank You For Playing Quiz Master!")