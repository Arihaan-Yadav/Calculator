import os 
import math
def calc_root():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------")
    print("-------------CALCULATOR-------------")
    print("------------------------------------")

    while True:
        while True:
            try:
                num = int(input("Enter a number: "))
                break
            except ValueError:
                print("Invalid! (Do NOT use decimal numbers.)")

        while True:
            try:
                root_num = int(input("Enter an integer n (number root n): "))
                if root_num == 0:
                    print("Invalid! (Math Error: root degree cannot be 0)")
                    continue
                break
            except ValueError:
                print("Invalid! (Do NOT use decimal numbers.)")

        if num < 0:
            if root_num % 2 == 0:
                print("Math Error: even root of a negative number is not real.")
                continue
            try:
                result = -(abs(num) ** (1 / root_num))
            except (OverflowError, ValueError):
                print("Math Error: result is outside the supported numeric range.")
                continue
        else:
            if num == 0 and root_num < 0:
                print("Math Error: division by zero.")
                continue
            try:
                result = num ** (1 / root_num)
            except (OverflowError, ValueError):
                print("Math Error: result is outside the supported numeric range.")
                continue

        if not math.isfinite(result):
            print("Math Error: result is outside the supported numeric range.")
            continue

        print(f"Answer: {result:.12g}")
        break
