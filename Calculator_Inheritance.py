#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 8
#Create a new class that inherits from existing class in your calculator program - Add new method(s) or override an existing method(s) in the new class
# - Use the new class and the new method in your calculator program

#Imports necessary elements
import tkinter as tkinter
from tkinter import messagebox
import math
from Simple_app_calculator import calculator
from tkinter import ttk
from Calculator_GUI import calculator_GUI

#creates child class
class ScientificCalculator(calculator):
    #allows child class to  inherit and utilize the attributes of parent class
    def __init__(self):
        super().__init__()
    #Adds new power method
    def operation_power(self, num_1, num_2):
        #Exception handling for errors if num_1 and num_2 is not integer
        try:
            if not isinstance(num_1, int):
                raise TypeError
            elif not isinstance(num_2, int):
                raise TypeError
        #creates popup error message for Type Errors
        except TypeError:
            messagebox.showerror("TypeError", "Number and power must be integers")
        else:
            #calculates with power operation
            result = num_1 ** num_2
            self.result = result
            return
    #adds new square root method
    def operation_square_root(self, num_1):
        try:
            #Exception handling for errors if num_1 is not integer and less than 0
            if not isinstance(num_1, int):
                raise TypeError
            elif num_1 < 0:
                raise ValueError
            #creates popup error message for Type Errors
        except TypeError:
            messagebox.showerror("TypeError", "Number must be a positive integer")
            #creates popup error message for Value Errors
        except ValueError:
            messagebox.showerror("ValueError", "Number must be a positive integer")
        else:
            #calculates with square root operation
            result = math.sqrt(num_1)
            self.result = result
            return

#Creates child class for GUI
    #Overrides __init__ to add options for power and squareroot operation
    #override calculate results to add functions for power and squareroot operation
    #starts the event loop of the GUI application