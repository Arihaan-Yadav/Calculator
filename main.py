
# Start
from utils import calculator
from utils import compare
from utils import squares
from utils import roots
from utils import percentage
import os
import math

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Calculator")
        print("2. Compare 2 numbers")
        print("3. Squares")
        print("4. Roots")
        print("5. Percentage")
        
        choice = input("Choose an option (1/2/3/4/5): ").strip()
        
        if choice == "1":
            calculator.calculator()
            break
        elif choice == "2":
            compare.calc_compare()
            break
        elif choice == "3":
            squares.calc_square()
            break
        elif choice == "4":
            roots.calc_root()
            break
        elif choice == "5":
            percentage.calc_percentage()
            break
        else:
            print("Invalid choice! Please try entering your choice again.")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------")
    print("-------------CALCULATOR-------------")
    print("------------------------------------")
    print(" ")
    print(" ")
    main()
    print(" ")
    print("Thank You! Made by Arihaan Yadav.")
# End
