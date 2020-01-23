import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

difficulty = {'easy':100, 'medium':1000, 'hard':10000}

def start():
    print("Hello Welcome to the Number Game!!!")
    print("type difficulty: easy medium hard")
    dif = input()

    if dif == 'easy' or dif == 'medium' or dif == 'hard':
        num = random.randrange(difficulty[a])
        return guessinggame(intial(dif), num, difficulty[dif])
    else:
        print('Didnt type in properly. Please write either easy medium or hard properly')
        return start()

def intial(dif):
    if dif == 'easy':
        print('Chose a number between 0 and 100')
        guess = int(input())
        return guess
    elif dif == 'medium':
        print('Chose a number between 0 and 1000')
        guess = int(input())
        return guess
    elif dif == 'hard':
        print('Chose a number between 0 and 10000')
        guess = int(input())
        return guess
    
def guessinggame(guess, num, dif):

    count = 1

    while guess != num:

        if guess > num:
            if (guess - num) / dif >=
            phrases(1,)
            
        elif guess < num:

        else:
            pass

def phrases():

print("You guessed higher than the number")
print("You guessed lower than the number")

print("you are far off")
print("you are ")
print("you are very close")




#while b != num

print (start())