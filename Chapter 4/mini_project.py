"""
Set a random number and ask the user to guess 
it. Give hints if the guess is too high or too low.
"""
number = 47

while True:
    user_guess = int(input("Guess the number:"))
    if user_guess > number:
        print("Your guess is too high")
    elif user_guess < number:
        print("Your guess is too low")
    else:
        print("You have guessed the number")
        break