#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 7
#Redo calculator program applying the OOP concept previously discussed

#Imports necessary elements
import tkinter as tkinter
from tkinter import messagebox
#Creates calculator class
#Creates def for Non-Parametrized Constructor
#Creates def for on and off of calculator
#Creates def for all operations
#Creates def for Input of num1 & num2
def calculate():
     # def for performing the addition operation 
    if operation == 1:
        result = num1 + num2
        result_label.config(text="Result: " + str(result))
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


