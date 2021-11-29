import random

while True:
    try:
        top_of_range = int(input("Please type in max number: "))
        break
    except ValueError as v:
        print("There is a value error in your max number. Please try again.")

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    try:
        guesses += 1
        user_guess = input("Make a Guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time.")
            continue
        
        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    except ValueError as v:
        print("Please make sure you are only typing in a number")

print("Print you got it in", guesses, "guesses")
