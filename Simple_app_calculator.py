#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 7
#Redo calculator program applying the OOP concept previously discussed

#Imports necessary elements
import tkinter as tkinter
from tkinter import messagebox
#Creates calculator class
class calculator():
    #Creates def for Non-Parametrized Constructor
    def __init__(self):
        self.num_1=0
        self.num_2=0
        self.on = False
        self.result=0
    #Creates def for on and off of calculator
    def turn_On(self):
        self.on = True

    def turn_Off(self):
        self.on = False
     # def for performing the addition operation 
    def operation_addition(self,num_1,num_2):
        try:
            if not isinstance(num_1, int):
                raise TypeError
            elif not num_1:
                raise ValueError
        except TypeError:
            messagebox.showerror("TypeError", "Number 1 must be an integer")
        except ValueError:
            messagebox.showerror("ValueError", "Number 1 must be an integer")
        else:
            result = self.num_1 + self.num_2
            self.result=result
            return
    # def for performing the subtraction operation 
    elif operation == 2:
        result = num1 - num2
        result_label.config(text="Result: " + str(result))
    # def for performing the multiplication operation 
    elif operation == 3:
        result = num1 * num2
        result_label.config(text="Result: " + str(result))
    # def for performing the division operation 
    elif operation == 4:
        try:
            result = num1 / num2
            result_label.config(text="Result: " + str(result))
        #Does not allow zero division
        except ZeroDivisionError:
            num2_entry.delete(0, tkinter.END)
            return messagebox.showerror("Error on Second Number Entry", "Invalid Input, Cannot Divide by Zero")
# Asking user if they want to try again or not
    choice = messagebox.askyesno("Try again?", "Do you want to try again?")
    #Creates a pop-up Thank you message and closes the program
    if not choice:
        messagebox.showinfo("Thank you message", "Thank you!")
        window.destroy()
    #Creates def for Input of num1 & num2

