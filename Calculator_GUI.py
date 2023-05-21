#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 7
#Redo calculator program applying the OOP concept previously discussed

#Imports necessary elements
import tkinter as tkinter
from tkinter import messagebox
from Simple_app_calculator import calculator
from tkinter import ttk
#Creates class for calculator GUI
calc = calculator()
class calculator_GUI:
    #Creates def for Parametrized Constructor and GUI
    def __init__(self, calc, GUI):
        self.GUI = GUI
        self.calc= calc

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
        options = ["1-Additon", "2-Subtraction", "3-Multiplication", "4-Division"]
        self.calc.selected_option = tkinter.StringVar()
        self.calc.combo = ttk.Combobox(GUI, textvariable=self.calc.selected_option)
        self.calc.combo['values'] = options
        self.calc.combo.pack()
        self.calc.combo.set("Select an operation")

        #Label and textbox for results
        self.calc.results_label = tkinter.Label(GUI, text="Results:")
        self.calc.results_label.pack(pady=5)
        self.calc.results_entry = tkinter.Entry(GUI)
        self.calc.results_entry.pack(pady=5)
        
        #Button to calculate results
        self.calc.prints_results = tkinter.Button(GUI, text="Caculate", command=self.calculate_results)
        self.calc.prints_results.pack(pady=10)
#Def for button functions
    #def for power button command
    def toggle_power(self):
        if self.calc.on:
            self.calc.turn_Off()
            self.calc.power_button.config(text="Power: Off")
        else:
            self.calc.turn_On()
            self.calc.power_button.config(text="Power: On")

    def enter_num1 (self):
        try:
            if not self.calc.on:
                messagebox.showinfo("Error", "Please turn on the Power")
                return
            num_1 = self.calc.num1_entry.get()
            if not num_1:
                messagebox.showinfo("Error", "Please enter a value for Number 1")
                return

            if not num_1.isdigit():
                raise ValueError

            self.calc.set_num1(int(num_1))
        except ValueError:
            messagebox.showerror("ValueError", "Number must be an integer")

    def enter_num2 (self):
        if not self.calc.on:
            messagebox.showinfo("Error", "Please turn on the Power")
            return
        num_2 = self.calc.num2_entry.get()
        self.calc.set_num2(int(num_2))
 
    def calculate_results(self):
        selected_item = self.calc.combo.get()
        num_1 = self.calc.get_num1()
        num_2 = self.calc.get_num2()
        if selected_item[0] == '1':
            self.calc.operation_addition(num_1, num_2)
            results = self.calc.get_results()
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))
        elif selected_item[0] == '2':
            self.calc.operation_subtraction(num_1, num_2)
            results = self.calc.get_results()
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))
        elif selected_item[0] == '3':
            self.calc.operation_multiplication(num_1, num_2)
            results = self.calc.get_results()
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))
        elif selected_item[0] == '4':
            self.calc.operation_division(num_1, num_2)
            results = self.calc.get_results()
            self.calc.results_entry.delete(0, tkinter.END)
            self.calc.results_entry.insert(0, str(results))
    #Def for asking user if they want to try again or not
#starts the event loop of the GUI application
GUI = tkinter.Tk()
GUI.title("Calculator")
GUI_calculator= calculator_GUI(calc, GUI)
GUI.mainloop()