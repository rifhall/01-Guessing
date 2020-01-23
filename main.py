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
        num = random.randrange(difficulty[dif])

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

        #This is code for if they ever guess outside of the range
        while guess <= 0 or guess > 100:
            print("Please chose an number within the range")
            guess = int(input())
        return guess

    elif dif == 'medium':
        print('Chose a number between 0 and 1000')
        guess = int(input())
        while guess <= 0 or guess > 1000:
            print("Please chose an number within the range")
            guess = int(input())
        return guess

    elif dif == 'hard':
        print('Chose a number between 0 and 10000')
        guess = int(input())
        while guess <= 0 or guess > 10000:
            print("Please chose an number within the range")
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
            if (guess - num) / dif >= 0.5:
                phrases(1,0)
            elif ((guess - num) / dif < 0.5) and ((guess - num) / dif > 0.15):
                phrases(1,1)
            else:
                phrases(1,2)


        #this is if they guess lower gives a different response based on how well the guess was
        elif guess < num:
            if (guess - num) / dif >= 0.5:
                phrases(0,0)
            elif ((guess - num) / dif < 0.5) and ((guess - num) / dif > 0.15):
                phrases(0,1)
            else:
                phrases(0,2)
        
        #this is the new guess they make and an update to the counter
        print("what is your new guess?")
        guess = int(input())
        while guess <= 0 or guess > dif:
            print("Please chose an number within the range")
            guess = int(input())
        count += 1
    
    #this is when the while loop is finished and youve gotten the right awnser
    print("Youve guessed the right number!!!")
    
    #A vairable response based on your count
    if count == 1:
        print("Congrats, it only took you " + str(count) + " guess to get the awnser.")
    elif count > 1 and count <= 5:
        print("it took you " + str(count) + " guesses to get the awnser. Good work!")
    elif count > 5 and count <= 10:
        print("it took you " + str(count) + " guesses to get the awnser. Not Bad!")
    elif count > 10 and count <= 20:
        print("it took you " + str(count) + " guesses to get the awnser. You can do better. ")
    else:
        print("it took you " + str(count) + " guesses to get the awnser. You may want to try an easier difficulty")

    


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

    
    

start()