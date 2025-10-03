try:
    num1 = 5
    num2 = 0

    division = num1 / num2

    print(division)

except ZeroDivisionError as e:
    print(f'Error occured: {e}')

finally:
    print("Execution complete")