print("Welcome to my Quiz Game. ")
print()
marks = 10 
#lets know if they want to play
play = input("Do you want to play my quiz game ? (yes/no) ")
if play != "yes":
    quit()
print("Ok let's play! ")
print()
print('your total score is 10marks, you loose 2 marks for each question you fail. ')
print()
#the first question
marks = -2
answer1 = input("what doed A.I stand for ? ")
print()
if answer1 .lower()== "artificial intelligence":
    print('correct answer')
else:
    print('you just lost',marks, "marks, keep trying")
# the second question
answer1 = input("what doed DEFi stand for ? ").lower()
print()
if answer1 .lower()== "decentralized finance":
    print('correct answer')
else:
    print('your answer is wrong, you just lost', marks,"keep trying")

# third question
marks = -2
answer1 = input("what does DAO's stand for ? ")
print()
if answer1 .lower() == "decentralized autonomous organizations":
    print('correct answer')
    print()
else:
    print('your answer is wrong. you just lost', marks, "think before answering")
# the fourth question
answer1 = input("what would you buy with your last $1 ? ")
if answer1.lower == "anything":
    print('correct answer')
#else:
 #   print('your answer is wrong. ')


# the fifth question
answer1 = input("what would you do if you found yourself at the peak of a mountain, about to fall off? ").lower()
if answer1 .lower() == "jump off and die" or "find a way to get out of the mountain":
    print('that"s good to know')
    print()
    print("you got" + str(marks) + "marks left")
    quit()