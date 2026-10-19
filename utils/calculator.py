import os
import math

def calculator():
    def read_finite_number(prompt):
        while True:
            try:
                number = float(input(prompt))
                if math.isfinite(number):
                    return number
                print("Invalid! Enter a finite number.")
            except ValueError:
                print("Invalid!")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------")
    print("-------------CALCULATOR-------------")
    print("------------------------------------")
    first_num = read_finite_number("Enter first number: ")

    while True:
        operation = input("Enter operation. Choose from (a)ddition, (s)ubtraction, (m)ultiplication, and (d)ivision: ").strip().lower()
        if operation != "s" and operation != "a" and operation != "m" and operation != "d":
            print("Invalid!")
        else:
            break

    while True:
        second_num = read_finite_number("Enter second number: ")
        if operation == "d" and second_num == 0:
            print("Math Error: cannot divide by zero.")
            continue
        break

    try:
        if operation == "a":
            answer = first_num + second_num
        elif operation == "s":
            answer = first_num - second_num
        elif operation == "m":
            answer = first_num * second_num
        else:
            answer = first_num / second_num

        if math.isfinite(answer):
            print(f"Answer: {answer}")
        else:
            print("Math Error: result is outside the supported numeric range.")
    except OverflowError:
        print("Math Error: result is outside the supported numeric range.")
