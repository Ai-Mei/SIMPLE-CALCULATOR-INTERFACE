from OPERATIONS import Operation
from tkinter import messagebox

class NewCalculator:
    def addition(self, num_1, num_2):
        try:
            answer = num_1 + num_2
            return f"The sum of the two numbers: {answer}"
        except TypeError:
            # Input is not a valid number
            return f"⚠️ Please enter 2 numbers."
            
    def subtraction(self, num_1, num_2):
        try:
            answer = num_1 - num_2
            return f"The difference of the two numbers: {answer}"
        except TypeError:
            # Input is not a valid number
            return f"⚠️ Please enter 2 numbers."
        
    def multiplication(self, num_1, num_2):
        try:
            answer = num_1 * num_2
            return f"The product of the two numbers: {answer}"
        except TypeError:
            # Input is not a valid number
            return f"⚠️ Please enter 2 numbers."

    def division(self, num_1, num_2):
        try:
            answer = num_1 / num_2
            remainder = num_1 % num_2
            return f"The quotient of the two numbers: {answer}\nThe remainder of number 1 / number2 is: {remainder}"
        except ZeroDivisionError:
            return "⚠️ Error, the number is divided by 0."
        except TypeError:
            # Input is not a valid number
            return f"⚠️ Please enter 2 numbers."
        
    # Added a method for raising a number to nth number.
    def raise_to_nth_power(self, num_1, num_2):
        try:
            answer = num_1 ** num_2
            return f"{num_1} raised to the power of {num_2} is: {answer}"
        except ValueError:
            return f"⚠️ Error, invaldid input."
        except TypeError:
            # Input is not a valid number
            return f"⚠️ Please enter 2 numbers."

        