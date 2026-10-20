import os
import math

def calc_percentage():
    from fractions import Fraction

    def read_float(prompt):
        while True:
            try:
                number = float(input(prompt))
                if math.isfinite(number):
                    return number
                print("Invalid!")
            except ValueError:
                print("Invalid!")

    def read_positive_integer(prompt):
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number
                print("Invalid!")
            except ValueError:
                print("Invalid!")

    def read_nonnegative_float(prompt):
        while True:
            number = read_float(prompt)
            if number >= 0:
                return number
            print("Value cannot be negative!")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------")
    print("-------------CALCULATOR-------------")
    print("------------------------------------")
    print("What do you want to calculate?")

    print("1. Percentage")
    print("2. Profit and loss")
    print("3. Simple interest")
    
    while True:
        try:
            mode_select = int(input("Select: "))
            if mode_select in (1, 2, 3):
                break
            else:
                print("Invalid!")
        except ValueError:
            print("Invalid!")

    if mode_select == 1:
        os.system("cls" if os.name == "nt" else "clear")
        print("------------------------------------")
        print("-------------CALCULATOR-------------")
        print("------------------------------------")
        print("What do you want to calculate?")
        print("1. Fraction and percentage")
        print("2. Decimal and percentage")
        print("3. Ratio and percentage")
        print("4. Exam percentage")

        while True:
            try:
                percentage_mode = int(input("Select: "))
                if percentage_mode in (1, 2, 3, 4):
                    break
                print("Invalid!")
            except ValueError:
                print("Invalid!")

        if percentage_mode in (1, 2, 3):
            print("1. Convert to percentage")
            print("2. Convert from percentage")
            while True:
                try:
                    conversion_direction = int(input("Select: "))
                    if conversion_direction in (1, 2):
                        break
                    print("Invalid!")
                except ValueError:
                    print("Invalid!")

        if percentage_mode == 1:
            if conversion_direction == 1:
                numerator = read_float("Enter fraction numerator: ")
                while True:
                    denominator = read_float("Enter fraction denominator: ")
                    if denominator != 0:
                        break
                    print("Denominator cannot be zero!")
                fraction = numerator / denominator
                print(f"Answer: {fraction * 100:.10g}%")
            else:
                percent = read_float("Enter percentage: ")
                fraction = Fraction(str(percent)) / 100
                print(f"Answer: {fraction}")
        elif percentage_mode == 2:
            if conversion_direction == 1:
                decimal = read_float("Enter decimal: ")
                print(f"Answer: {decimal * 100:.10g}%")
            else:
                percent = read_float("Enter percentage: ")
                print(f"Answer: {percent / 100:.10g}")
        elif percentage_mode == 3:
            if conversion_direction == 1:
                while True:
                    ratio_input = input("Enter ratio (e.g. 3:4): ").strip()
                    ratio_parts = ratio_input.split(":")
                    if len(ratio_parts) == 2:
                        try:
                            first_part = float(ratio_parts[0])
                            second_part = float(ratio_parts[1])
                            if (math.isfinite(first_part) and math.isfinite(second_part)
                                    and first_part >= 0 and second_part > 0):
                                break
                        except ValueError:
                            pass
                    print("Enter a valid ratio with a non-negative first part and positive second part.")
                percent = first_part / second_part * 100
                print(f"Answer: {percent:.10g}%")
            else:
                while True:
                    percent = read_float("Enter percentage (0 or more): ")
                    if percent >= 0:
                        break
                    print("Percentage cannot be negative!")
                percent_fraction = Fraction(str(percent))
                ratio = percent_fraction / 100
                print(f"Answer: {ratio.numerator}:{ratio.denominator}")
        elif percentage_mode == 4:
            paper_count = read_positive_integer("Enter number of papers: ")
            while True:
                marks_input = input("Marks possible in each paper [80]: ").strip()
                try:
                    marks_per_paper = 80.0 if marks_input == "" else float(marks_input)
                    if math.isfinite(marks_per_paper) and marks_per_paper > 0:
                        break
                    print("Marks per paper must be greater than zero!")
                except ValueError:
                    print("Invalid!")

            marks_obtained = Fraction(0)
            for paper_number in range(1, paper_count + 1):
                while True:
                    paper_marks = read_float(
                        f"Enter marks obtained in paper {paper_number}: "
                    )
                    if 0 <= paper_marks <= marks_per_paper:
                        marks_obtained += Fraction(str(paper_marks))
                        break
                    print(f"Marks must be between 0 and {marks_per_paper:g}!")

            total_marks = Fraction(str(marks_per_paper)) * paper_count
            score_fraction = marks_obtained / total_marks
            print(
                f"Total marks: {float(marks_obtained):.10g} / "
                f"{float(total_marks):.10g}"
            )
            print(f"Score fraction: {score_fraction}")
            print(f"Exam percentage: {float(score_fraction * 100):.10g}%")
    elif mode_select == 2:
        os.system("cls" if os.name == "nt" else "clear")
        print("------------------------------------")
        print("-------------CALCULATOR-------------")
        print("------------------------------------")
        print("What do you want to calculate?")
        print("1. Profit/Loss")
        print("2. Selling price or SP")
        print("3. Cost Price or CP")
        while True:
            try:
                mode_selection = int(input("Select: "))
                if mode_selection not in (1, 2, 3):
                    print("Invalid!")
                else:
                    break
            except ValueError:
                print("Invalid!")
        if mode_selection == 1:
            os.system("cls" if os.name == "nt" else "clear")
            print("------------------------------------")
            print("-------------CALCULATOR-------------")
            print("------------------------------------")

            cost_price = read_nonnegative_float("Enter Cost Price: ")
            selling_price = read_nonnegative_float("Enter Selling Price: ")

            if selling_price > cost_price:
                print("Since SP > CP, there is profit!")
                print(f"Answer: {selling_price - cost_price}")
            elif selling_price == cost_price:
                print("Since SP = CP, there is no profit and no loss")
                print("Therefore, answer: 0")
            elif selling_price < cost_price:
                print("Since CP > SP, there is loss!")
                print(f"Answer: {cost_price - selling_price}")
        elif mode_selection == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------")
            print("-------------CALCULATOR-------------")
            print("------------------------------------")
            cost_price = read_nonnegative_float("Enter cost price: ")
            while True:
                gain_or_loss = input("Is there a gain or loss percent?: ").strip().lower()
                if gain_or_loss in ("gain", "loss"):
                    break
                else:
                    print("Invalid!")
            if gain_or_loss == "gain":
                gain_percent = read_nonnegative_float("Enter gain %: ")
                print(f"Answer: {cost_price * (100 + gain_percent) / 100}")
            elif gain_or_loss == "loss":
                while True:
                    loss_percent = read_float("Enter loss %: ")
                    if 0 <= loss_percent <= 100:
                        break
                    print("Loss percent must be between 0 and 100!")
                print(f"Answer: {cost_price * (100 - loss_percent) / 100}")
            else:
                pass
        elif mode_selection == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------")
            print("-------------CALCULATOR-------------")
            print("------------------------------------")
            selling_price = read_nonnegative_float("Enter selling price: ")
            while True:
                gain_or_loss = input("Is there a gain or loss percent?: ").strip().lower()
                if gain_or_loss in ("gain", "loss"):
                    break
                else:
                    print("Invalid!")
            if gain_or_loss == "gain":
                gain_percent = read_nonnegative_float("Enter gain %: ")
                print(f"Answer: {selling_price * 100 / (100 + gain_percent)}")
            elif gain_or_loss == "loss":
                while True:
                    loss_percent = read_float("Enter loss % (less than 100): ")
                    if 0 <= loss_percent < 100:
                        break
                    print("Loss percent must be between 0 and 100, but not 100!")
                print(f"Answer: {selling_price * 100 / (100 - loss_percent)}")
            else:
                pass

    elif mode_select == 3:
        def read_choice(prompt, choices):
            while True:
                try:
                    choice = int(input(prompt))
                    if choice in choices:
                        return choice
                except ValueError:
                    pass
                print("Invalid!")

        def divide(numerator, denominator):
            if not math.isfinite(numerator) or not math.isfinite(denominator):
                print("Math Error: result is outside the supported numeric range.")
                return None
            if denominator == 0:
                print("Math Error: cannot calculate because the divisor is zero.")
                return None
            result = numerator / denominator
            if not math.isfinite(result):
                print("Math Error: result is outside the supported numeric range.")
                return None
            return result

        os.system('cls' if os.name == 'nt' else 'clear')
        print("------------------------------------")
        print("-------------CALCULATOR-------------")
        print("------------------------------------")
        print("What do you want to calculate?")
        print("1. Simple interest or total amount")
        print("2. Principal, time, or rate")
        selection_si = read_choice("Select: ", (1, 2))

        if selection_si == 1:
            os.system("cls" if os.name == "nt" else "clear")
            print("------------------------------------")
            print("-------------CALCULATOR-------------")
            print("------------------------------------")
            principal = read_float("Enter principal amount: ")
            rate = read_float("Enter rate per annum: ")
            time_sim_int = read_float("Enter time (in years): ")

            simple_interest = principal * rate * time_sim_int / 100
            if not math.isfinite(simple_interest):
                print("Math Error: simple interest is outside the supported numeric range.")
                return

            print("What do you want to show?")
            print("1. Total amount")
            print("2. Simple interest")
            print("3. Both")
            total_or_si = read_choice("Select: ", (1, 2, 3))

            if total_or_si in (1, 3):
                total_amount = principal + simple_interest
                if not math.isfinite(total_amount):
                    print("Math Error: total amount is outside the supported numeric range.")
                    return
            if total_or_si == 1:
                print(f"Answer: {total_amount:.10g}")
            elif total_or_si == 2:
                print(f"Answer: {simple_interest:.10g}")
            else:
                print(f"Simple interest: {simple_interest:.10g}")
                print(f"Total amount: {total_amount:.10g}")

        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("------------------------------------")
            print("-------------CALCULATOR-------------")
            print("------------------------------------")
            print("What do you want to calculate?")
            print("1. Principal amount")
            print("2. Time")
            print("3. Rate per annum")
            unknown = read_choice("Select: ", (1, 2, 3))

            print("What information do you have?")
            print("1. Simple interest")
            print("2. Total amount")
            known_value = read_choice("Select: ", (1, 2))

            if known_value == 1:
                simple_interest = read_float("Enter simple interest: ")
            else:
                total_amount = read_float("Enter total amount: ")

            if unknown == 1:
                if known_value == 1:
                    rate = read_float("Enter rate per annum: ")
                    time_sim_int = read_float("Enter time (in years): ")
                    principal = divide(
                        simple_interest * 100, rate * time_sim_int
                    )
                else:
                    rate = read_float("Enter rate per annum: ")
                    time_sim_int = read_float("Enter time (in years): ")
                    growth_factor = 1 + rate * time_sim_int / 100
                    principal = divide(total_amount, growth_factor)
                if principal is not None:
                    print(f"Principal: {principal:.10g}")

            elif unknown == 2:
                principal = read_float("Enter principal amount: ")
                rate = read_float("Enter rate per annum: ")
                if known_value == 1:
                    numerator = simple_interest * 100
                else:
                    numerator = (total_amount - principal) * 100
                time_sim_int = divide(numerator, principal * rate)
                if time_sim_int is not None:
                    print(f"Time: {time_sim_int:.10g} years")

            else:
                principal = read_float("Enter principal amount: ")
                time_sim_int = read_float("Enter time (in years): ")
                if known_value == 1:
                    numerator = simple_interest * 100
                else:
                    numerator = (total_amount - principal) * 100
                rate = divide(numerator, principal * time_sim_int)
                if rate is not None:
                    print(f"Rate per annum: {rate:.10g}%")

if __name__ == "__main__":
    calc_percentage()
