#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 7
#Redo calculator program applying the OOP concept previously discussed

#Imports necessary elements
import tkinter as tkinter
from tkinter import messagebox
from Simple_app_calculator import calculator
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
        if not self.calc.on:
            messagebox.showinfo("Error", "Please turn on the Power")
            return
        num_1 = self.calc.num1_entry.get()
        self.calc.set_num1(int(num_1))

    def enter_num2 (self):
        if not self.calc.on:
            messagebox.showinfo("Error", "Please turn on the Power")
            return
        num_2 = self.calc.num2_entry.get()
        self.calc.set_num2(int(num_2))
 
    #Def for asking user if they want to try again or not
#starts the event loop of the GUI application