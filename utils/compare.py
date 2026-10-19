import os

def calc_compare():
    os.system("cls" if os.name == "nt" else "clear")
    print("------------------------------------")
    print("-------------CALCULATOR-------------")
    print("------------------------------------")
    while True:
        try:
            first_num = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid!")
    while True:
        try:
            second_num = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid!")

    if first_num == second_num:
        print(f"{first_num} = {second_num}")
    elif first_num > second_num:
        print(f"{first_num} > {second_num}")
    elif first_num < second_num:
        print(f"{first_num} < {second_num}")
    else:
        pass