print("Welcome to the Quiz Game!")

name = input("Enter your name: ")
print("Hello", name, "! Let's start the quiz.\n")

score = 0

q1 = input("1. What is the capital of France? ")
if q1.lower() == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")

q2 = input("2. What is 5 + 3? ")
if q2 == "8":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 8.\n")

q3 = input("3. Which language is used for programming? (python/java/html) ")
if q3.lower() == "python":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Python.\n")

print("Your final score is:", score)

if score == 3:
    print("Excellent! You handled all scenarios perfectly.")
elif score == 2:
    print("Good job! Just a small mistake.")
elif score == 1:
    print("You need more practice.")
else:
    print("Try again and improve your knowledge.")

