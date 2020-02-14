import random

guesstaken=0

num = random.randint(1,20)

myname = input("Hello there!\nI'm Python\nWhat is your name? ")
print()
print("Well,"+myname+",I am thinking of a number between 1 to 20")

print()

while guesstaken < 6:
    print('Take a guess.')
    guess = int(input())
    guesstaken+=1

    if guess>num:
        print("oh.. Your Guess is too high.")
        print()
        
    if guess<num:
        print("amm.... Your Guess is too low.")
        print()
        
    if guess==num:
        break
if guess==num:
    print("Good job, "+myname+" ! You guessed my number in just "+str(guesstaken)+" guesses!")

    ans3=input()

if guess!=num:
    print("Nope. The number I was thinking of was "+str(num))
        

