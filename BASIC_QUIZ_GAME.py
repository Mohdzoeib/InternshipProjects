# Python quiz game

class questions :
    Questions = ("What is the capital of Italy ?",
                 "In which year did the India first won its cricket world cup ?",
                 "Who has the most followers on Instagram ?",
                 "Who invented Theory of relativity ?",
                 "In which year was The Godfather first released?",
                 )
class options :
    Options = (("A. France ","B. Rome ","C. China ","D. Delhi"),
               ("A. 2011 ","B. 2019 ","C. 1975 ","D. 1983 "),
               ("A. therock ","B. leomessi ","C. cristiano ","D. justinbieber "),
               ("A. Albert Einsetein ","B. Isaac Newton ","C. Thomas Edison ","D. Stephen Hawking "),
               ("A. 2022 ","B. 1985 ","C. 1978 ","D. 1972 "))

Answers = ("B","D","C","A","D")
score = 0
question_num = 0

for question in questions.Questions:
    print("----------------------------------------------------------")
    print(question)
    for option in options.Options[question_num]:
        print(option)
     
    guess = input("Enter (A,B,C,D):").upper()
    if guess == Answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("invlaid")
        print(f"{Answers[question_num]} is a Correct answer ")
    question_num += 1
    
print("---------------------------------------")
print("               Results                 ")
print("---------------------------------------")

score = int(score / len(questions.Questions) * 100)

print(f"Your score is: {score}%")
