# rows = int(input("enter your rows:"))
# cols = int(input("Enter your cols:"))
# sym  = input("Enter the symbol:")
# for i in range(rows):
#     for j in range(cols):
#         print(sym,end=" ")
#     print()

# r = int(input("enter the rows:"))
# c = int(input("Enter the cols:"))
# dialpad="* 0 #"
# count = 1;
# for i in range(r):
#     for j in range(c):
#          print(count,end= " ")
#          count+=1
#     print()
# print(dialpad)


# dialpad = [
#     ["1", "2", "3"],
#     ["4", "5", "6"],
#     ["7", "8", "9"],
#     ["*", "0", "#"]
# ]

# for row in dialpad:
#     for item in row:
#         print(item, end=" ")
#     print()

#compound interest task
# principal = float(input("enter the principal amount: "))
# rate = float(input("enter rate percentage: "))
# time = int(input("enter no.of years: "))
# amount = principal*(1+rate/100)**time
# print("compound interest is: ",amount-principal)

#random number guessing
# import random
# number = random.randint(1,100)
# while True:
#     guess = int(input("guess a number between 1 and 100: "))
#     if guess == number:
#         print("you guessed the number correctly")
#         break
#     elif guess < number:
#         print("Too low try again!")
#     else:
#         print("Too high try again!")    

#rock, paper, scissor game
import random
choices = ["rock", "paper", "scissors"]
while True:
    computer = random.choice(choices)
    user = input("Enter rock, paper, or scissors: ")
    if user == computer:
        print("It's a tie")
    elif(user == "rock" and computer =="scissors")or\
        (user == "paper" and computer =="rock")or\
        (user == "scissors" and computer =="paper"):
        print("you wins")
    elif user in choices:
       print("computer wins")
    else:
        print("choice is invalid")
    print("computer chose: ", computer)
    play = input("Play again? (yes/no): ")
    if play!= "yes":
        print("game over!")
        break