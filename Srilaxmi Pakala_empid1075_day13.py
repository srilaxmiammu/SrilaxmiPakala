import logging
from datetime import datetime
from collections import Counter

logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidChoiceError(Exception):
    pass


class SecureCalculatorPro:

    def __init__(self):
        self.history_file = "history.txt"
        self.error_types = []
        self.total_calculations = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def save_history(self, record):
        with open(self.history_file, "a") as file:
            file.write(record + "\n")

    def perform_calculation(self):

        try:
            print("\nOperations")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = int(input("Enter choice (1-4): "))

            if choice not in [1, 2, 3, 4]:
                raise InvalidChoiceError("Invalid operation selected.")

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                result = self.add(a, b)
                operation = f"{a} + {b}"

            elif choice == 2:
                result = self.subtract(a, b)
                operation = f"{a} - {b}"

            elif choice == 3:
                result = self.multiply(a, b)
                operation = f"{a} * {b}"

            else:
                result = self.divide(a, b)
                operation = f"{a} / {b}"

        except ValueError:
            print("Error: Please enter valid numeric values.")
            logging.error("ValueError - Invalid numeric input")
            self.error_types.append("ValueError")

        except ZeroDivisionError as e:
            print("Error:", e)
            logging.error(str(e))
            self.error_types.append("ZeroDivisionError")

        except InvalidChoiceError as e:
            print("Error:", e)
            logging.error(str(e))
            self.error_types.append("InvalidChoiceError")

        else:
            print("Result =", result)

            record = f"{datetime.now()} | {operation} = {result}"

            self.save_history(record)
            self.total_calculations += 1

        finally:
            print("Calculation process completed.\n")

    def view_history(self):
        try:
            with open(self.history_file, "r") as file:
                data = file.read()

                if data.strip():
                    print("\n===== CALCULATION HISTORY =====")
                    print(data)
                else:
                    print("No history available.")

        except FileNotFoundError:
            print("History file not found.")

    def view_error_report(self):
        try:
            with open("error_log.txt", "r") as file:
                data = file.read()

                if data.strip():
                    print("\n===== ERROR REPORT =====")
                    print(data)
                else:
                    print("No errors recorded.")

        except FileNotFoundError:
            print("No error log file found.")

    def generate_summary(self):

        total_errors = len(self.error_types)

        if self.error_types:
            most_common = Counter(self.error_types).most_common(1)[0][0]
        else:
            most_common = "No Errors"

        print("\n===== SUMMARY REPORT =====")
        print("Total Calculations :", self.total_calculations)
        print("Total Errors       :", total_errors)
        print("Most Common Error  :", most_common)


def main():

    calculator = SecureCalculatorPro()

    while True:

        print("\n========== SECURE CALCULATOR PRO ==========")
        print("1. Perform Calculation")
        print("2. View Calculation History")
        print("3. View Error Report")
        print("4. Generate Summary Report")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                calculator.perform_calculation()

            elif choice == 2:
                calculator.view_history()

            elif choice == 3:
                calculator.view_error_report()

            elif choice == 4:
                calculator.generate_summary()

            elif choice == 5:
                print("Thank you for using Secure Calculator Pro.")
                break

            else:
                print("Invalid menu choice.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()