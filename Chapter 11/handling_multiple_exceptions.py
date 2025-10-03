try:
    age = '9' 
    new_age = int(age)

    print(4/0)

except ValueError as e:
    print(f'Error occured: {e}')

except ZeroDivisionError as e:
    print(f"You can't divide a number by 0: {e}")


"""
Write a program that:

Asks the user for two numbers.

Tries to divide the first number by the second.

Handles the following exceptions:

ValueError (if the input is not a number).

ZeroDivisionError (if dividing by zero).

Always prints "Program complete" at the end.

"""