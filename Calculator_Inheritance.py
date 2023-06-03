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
calc_2 = ScientificCalculator()
class Scicalculator_GUI(ScientificCalculator, calculator_GUI):
    #Overrides __init__ to add options for power and squareroot operation
    def __init__(self, calc_2, GUI):
        self.GUI = GUI
        self.calc= calc_2

        #Combobox for options of Models
        options_model = ["1-Casio", "2-Samsung", "3-Sony"]
        self.calc.selected_option_model = tkinter.StringVar()
        self.calc.combo_model = ttk.Combobox(GUI, textvariable=self.calc.selected_option_model)
        self.calc.combo_model['values'] = options_model
        self.calc.combo_model.pack()
        self.calc.combo_model.set("Select a Model")
        self.calc.combo_model.configure(state='readonly')

        #Button for Power on and off
        self.calc.power_button = tkinter.Button(GUI, text="Power: Off", command=self.toggle_power)
        self.calc.power_button.pack(pady=10)

        #Label, Text Box, and Button for Num1 Input
        self.calc.num1_label = tkinter.Label(GUI, text="Number 1:")
        self.calc.num1_label.pack(pady=5)
        self.calc.num1_entry = tkinter.Entry(GUI)
        self.calc.num1_entry.pack(pady=5)
        self.calc.num1_enter= tkinter.Button(GUI, text="Enter", command=self.enter_num1)
        self.calc.num1_enter.pack(pady=10)

        #Label, Text Box, and Button for Num1 Input
        self.calc.num2_label = tkinter.Label(GUI, text="Number 2:")
        self.calc.num2_label.pack(pady=5)
        self.calc.num2_entry = tkinter.Entry(GUI)
        self.calc.num2_entry.pack(pady=5)
        self.calc.num2_enter= tkinter.Button(GUI, text="Enter", command=self.enter_num2)
        self.calc.num2_enter.pack(pady=10)

        #Combobox for options of operations
        options = ["1-Additon", "2-Subtraction", "3-Multiplication", "4-Division", "5-Power", "6-Square root"]
        self.calc.selected_option = tkinter.StringVar()
        self.calc.combo = ttk.Combobox(GUI, textvariable=self.calc.selected_option)
        self.calc.combo['values'] = options
        self.calc.combo.pack()
        self.calc.combo.set("Select an operation")
        self.calc.combo.configure(state='readonly')

        #Label and textbox for results
        self.calc.results_label = tkinter.Label(GUI, text="Results:")
        self.calc.results_label.pack(pady=5)
        self.calc.results_entry = tkinter.Entry(GUI)
        self.calc.results_entry.pack(pady=5)
        
        #Button to calculate results
        self.calc.prints_results = tkinter.Button(GUI, text="Caculate", command=self.calculate_results)
        self.calc.prints_results.pack(pady=10)

        #Reference to check if there is a number input before calculating
        self.num1_calculate=0
        self.num2_calculate=0

        self.GUI.geometry("400x600")
    #override calculate results to add functions for power and squareroot operation
    def calculate_results(self):
        #Error message when calculator is off and tries to calculate
        if not self.calc.on:
            messagebox.showinfo("Error", "Please turn on the Power")
            return
                #Retrieves user's choice
        selected_item = self.calc.combo.get()
        operation_choice=int(selected_item[0])
        #Checks if there is a number input on both num1 and num2 if the chosen operation is not Squareroot
        if operation_choice<6 and (self.num1_calculate==0 or self.num2_calculate==0):
            messagebox.showinfo("Error", "Please enter your two numbers first")
            return
        if operation_choice==6 and self.calc.get_num2():
            self.calc.set_num2(0)
            self.calc.num2_entry.delete(0, tkinter.END)
            messagebox.showinfo("Reminder", "Only Number 1 will be used for the calculation")
            return
        #Checks if there is a number input on both num1 and num2
        if self.num1_calculate==0 or self.num2_calculate==0:
            messagebox.showinfo("Error", "Please enter your two numbers first")
            return
        #Shows error message if no operation selected
        if self.calc.selected_option.get() == "Select an operation":
            messagebox.showinfo("Error", "Please select an operation first")
            return

        #Retrieves numbers
        num_1 = self.calc.get_num1()
        num_2 = self.calc.get_num2()

        #If first choice, addition
        if selected_item[0] == '1':
            self.calc.operation_addition(num_1, num_2)
            results = self.calc.get_results()
            #Clears any previous input in results entry and replaces with current results
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))

        #If second choice, subtraction
        elif selected_item[0] == '2':
            self.calc.operation_subtraction(num_1, num_2)
            results = self.calc.get_results()
            #Clears any previous input in results entry and replaces with current results
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))

        #If third choice, multiplication
        elif selected_item[0] == '3':
            self.calc.operation_multiplication(num_1, num_2)
            results = self.calc.get_results()
            #Clears any previous input in results entry and replaces with current results
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))

        #If last choice, division
        elif selected_item[0] == '4':
            self.calc.operation_division(num_1, num_2)
            results = self.calc.get_results()
            #Clears any previous input in results entry and replaces with current results
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))

        #If fifth choice, power
        elif selected_item[0] == '5':
            self.calc.operation_power(num_1, num_2)
            results = self.calc.get_results()
            #Clears any previous input in results entry and replaces with current results
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))

        #If last choice, square root
        elif selected_item[0] == '6':
            self.calc.operation_square_root(num_1)
            results = self.calc.get_results()
            #Clears any previous input in results entry and replaces with current results
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))

        # Asking user if they want to try again or not
        choice = messagebox.askyesno("Try again?", "Do you want to try again?")
        #If no, creates a pop-up Thank you message and closes the program
        if not choice:
            messagebox.showinfo("Thank you message", "Thank you!")
            GUI2.destroy()
        #If yes, clears all initial input
        else:
            self.calc.num1_entry.delete(0, tkinter.END)
            self.calc.num2_entry.delete(0, tkinter.END)
            self.calc.selected_option.set("Select an operation")
            self.calc.results_entry.delete(0, tkinter.END)
            self.num1_calculate=0
            self.num2_calculate=0

    #starts the event loop of the GUI application
GUI2 = tkinter.Tk()
GUI2.title("Scientific Calculator")
GUI2_calculator= Scicalculator_GUI(calc_2, GUI2)
GUI2.mainloop()
