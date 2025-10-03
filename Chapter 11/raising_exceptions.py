age = int(input("Enter your age: "))

try:
    if age < 16:
        raise ValueError("You must be at least 16 to use this program")
    else:
        print("You are is valid")

except ValueError as e:
    print(f'Error occured: {e}')