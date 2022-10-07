import random
# Greet the user 
print("Hi, Welcome To My Number Guessing Game")
print('Please Choose Difficulty by typing number: 1.Very easy: 1-10 2.Easy: 5 tries 1-10 3.Medium: 5 tries 1-100 4.Difficult: 8 tries 1-500 5.Very difficult: 9 tries 1-1000')
# Get the difficulty
dif = input("Difficulty: ")
if dif == '1': #Very Easy Option
    #Randomly get a number from 1-10
    ran = random.randrange(int(1),int(11))
    guess = int(0)
    while int(guess) != int(ran):# if the guess isnt the randomly choosen answer ask again
        guess = input("Guess: ")
        if int(guess) == int(ran): #if theyre right congratulate them
            print("Congrats you won")
            break
        elif int(guess) < int(ran): # if number is too low tell them its too low
            print("Too low")
        elif int(guess) > int(ran): #if number is too high tell them its too high
            print("Too high")
        else:
            print("invalid")
elif dif == '2':#set up the same way
    ran = random.randrange(int(1),int(11))
    guess = int("0")
    # change the loop to only allow 5 guesses but the rest is the smae
    for x in range(4):
        guess = input("Guess: ")
        if int(guess) == int(ran):
            print("Congrats you won")
            break
        elif int(guess) < int(ran):
            print("Too low")
        elif int(guess) > int(ran):
            print("Too high")
        else:
            print("invalid")
    else: #since theres a limited amount of tries for this difficulty if they run out of guesses tell them the correct answer
        print("sorry you couldn't guess in time the answer was: " + str(ran))
elif dif == '3': # repeat just adjust the number of possible numbers
    ran = random.randrange(int(1),int(101))
    guess = int("0")
    for x in range(4): #this is for amount of attempts they get
        guess = input("Guess: ")
        if int(guess) == int(ran):
            print("Congrats you won")
            break
        elif int(guess) < int(ran):
            print("Too low")
        elif int(guess) > int(ran):
            print("Too high")
        else:
            print("invalid")
    else:
        print("sorry you couldn't guess in time the answer was: " + str(ran))
elif dif == '4': #repeat with changing the range
    ran = random.randrange(int(1),int(501))
    guess = int("0")
    for x in range(7):#change the range again
        guess = input("Guess: ")
        if int(guess) == int(ran):
            print("Congrats you won")
            break
        elif int(guess) < int(ran):
            print("Too low")
        elif int(guess) > int(ran):
            print("Too high")
        else:
            print("invalid")    
    else:
        print("sorry you couldn't guess in time the answer was: " + str(ran))
elif dif == "5":#repeat with changing range
    ran = random.randrange(int(1),int(1001))
    guess = int("0")
    for x in range(8):#repeat with changing try amount
        guess = input("Guess: ")
        if int(guess) == int(ran):
            print("Congrats you won")
            break
        elif int(guess) < int(ran):
            print("Too low")
        elif int(guess) > int(ran):
            print("Too high")
        else:
            print("invalid")
    else:
        print("sorry you couldn't guess in time the answer was: " + str(ran))
else:# print invalid if error
    print('Invalid')