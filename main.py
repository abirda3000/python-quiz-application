print("WELCOME TO QUIZ APPLICATION")
score = 0
correct_answers = ["A","B","C","A","A"]
print("What is the capital of Iraq:")
choose_country = input("""
A)Baghdad
B)Mosul
C)Basra
D)Erbil
Choose your answer:
"""
).capitalize()
if choose_country != correct_answers[0]:
    print("Wrong")
    print(f"The right answer is {correct_answers[0]}")
else:
    score += 1
    print("Correct answer")
print("Which language are you learning")
choose_language = input("""
A)Java
B)Python
C)C++
D)C#
Choose your answer:
"""
).capitalize()
if choose_language != correct_answers[1]:
    print("Wrong")
    print(f"The right answer is {correct_answers[1]}")
else:
    score += 1
    print("Correct answer")
print("How many days are there in one week")
choose_day = input("""
A)5
B)6
C)7
D)8
Choose your answer:
"""
).capitalize()
if choose_day != correct_answers[2]:
    print("Wrong")
    print(f"The right answer is {correct_answers[2]}")
else:
    score += 1
    print("Correct answer")
print("How many months are there in one year")
choose_days = input("""
A)12
B)9
C)6
D)0
Choose your answer:
"""
).capitalize()
if choose_days != correct_answers[3]:
    print("Wrong")
    print(f"The right answer is {correct_answers[3]}")
else:
    score += 1
    print("Correct answer")
print("Which one is the biggest planet")
choose_planet = input("""
A)Jupiter
B)Earth
C)Mars
D)Pluto
Choose your answer:
"""
).capitalize()
if choose_planet != correct_answers[4]:
    print("Wrong")
    print(f"The right answer is {correct_answers[4]}")
else:
    score += 1
    print("Correct answer")
print("Your total score is:",score)
