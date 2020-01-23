import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#dictionary for the difficulties
difficulty = {'easy':100, 'medium':1000, 'hard':10000}

#Where the game starts
def start():
    print("Hello Welcome to the Number Game!!!")
    print("type difficulty: easy medium hard")

    #player chosing difficulty
    dif = input()

    #game making the number
    if dif == 'easy' or dif == 'medium' or dif == 'hard':
        num = random.randrange(difficulty[a])

        #sends the information here and the info from intitial guess to the actual game
        return guessinggame(intial(dif), num, difficulty[dif])

    #does recursion until they put a correct awnser in or kill the game
    else:
        print('Didnt type in a correct response. Please write either easy medium or hard properly')
        return start()

#does the initial guess
def intial(dif):
    #makes decision based on game difficulty, returns the first guess
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
    

#this is where the magic happens and the game runs 
def guessinggame(guess, num, dif):

    #a counter to tell us how many times you had a guess (starts at one cause we did that in initial)
    count = 1

    #run a while loop until they get it right
    while guess != num:

        #this is for if they guess higher, gives a different response based on how well the guess was
        if guess > num:
            if (guess - num) / dif >= 0.5
                phrases(1,0)
            elif ((guess - num) / dif < 0.5) and ((guess - num) / dif > 0.25):
                phrases(1,1)
            else:
                phrases(1,2)


        #this is if they guess lower gives a different response based on how well the guess was
        elif guess < num:
            if (guess - num) / dif >= 0.5
                phrases(0,0)
            elif ((guess - num) / dif < 0.5) and ((guess - num) / dif > 0.25):
                phrases(0,1)
            else:
                phrases(0,2)
        
        #this is the new guess they make and an update to the counter
        print("what is your new guess?")
        guess = int(input())
        count += 1
    


        

#a reference function to the initial game. Will spit out responses based on how well you did
def phrases(highlo,place):

    if highlo == 1:
        print("You guessed higher than the number")
    elif highlo == 0:
        print("You guessed lower than the number")

    if place == 0:
        print(" and you are far off")
    elif place == 1:
        print(" and you are on your way")
    else:
        print(" and you are very close")


