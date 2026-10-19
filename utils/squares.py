import os

def calc_square():
    os.system('cls' if os.name == 'nt' else 'clear')        
    print("------------------------------------")
    print("-------------CALCULATOR-------------")
    print("------------------------------------")
    while True:
        try:
            square_base = int(input("Enter Base: "))
            if square_base < 0:
                print("Invalid!")
                continue
            break
        except ValueError:
            print("Invalid!")

    while True:
        try:
            square_exponent = int(input("Enter exponent: "))
            if square_exponent < 0:
                print("Invalid!")
                continue
            break
        except ValueError:
            print("Invalid!")

    print(f"Answer: {square_base ** square_exponent}")
