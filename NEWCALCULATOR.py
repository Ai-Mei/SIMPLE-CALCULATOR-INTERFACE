from OPERATIONS import Operation
from tkinter import messagebox
#import math module for square root.
import math


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
        
    def square_root(self, num_1):
        try:
            num_1 = float(num_1)
            # Check the number if it is positive or negative since we can only get the square root of positive integers.
            if num_1 < 0:
                raise ValueError("Input must be a non-negative number.")
                
            answer = math.sqrt(num_1)
            return f"The square root of {num_1}: {answer}"
            #return f"The square root of {num_1} is: {square_root}"
        except ValueError as e:
            return f"⚠️ Error, {str(e)}"

    def nth_root(self, num_1, num_2):
        try:
            num_1 = float(num_1)
            num_2 = float(num_2)
            
            if num_2 == 0:
                raise ValueError("We can not calculate the 0th root.")
                
            answer = num_1 ** (1 / num_2)
            return f"The {num_2}rd/th root of {num_1} is: {answer}"
        
        except ValueError as e:
            return f"⚠️ Error: {str(e)}"
        except TypeError:
            return f"⚠️ Please enter two numbers."

        
    def factorial(self, num_1):
        try:
            num_1 = int(num_1)
            if num_1 < 0:
                raise ValueError("Factorial is not defined for negative numbers.")
            elif not isinstance(num_1, int):
                raise TypeError("Please enter a whole number.")
                
            answer = 1
            for i in range(1, num_1 + 1):
                answer *= i
            
            return answer
            
        except ValueError as e:
            return f"⚠️ Error: {str(e)}"
        except TypeError as e:
            return f"⚠️ Error: {str(e)}"


    def percentage(self, num_1, num_2):
        try:
            answer = (num_2 / 100) * num_1
            return f"The {num_2}% of {num_1} is: {answer}"
        except ValueError:
            return f"⚠️ Invalid input. Please enter valid numbers."
