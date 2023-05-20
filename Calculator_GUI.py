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
#Def for button functions
    #def for power button command
    def toggle_power(self):
        if self.calc.on:
            self.calc.turn_Off()
            self.calc.power_button.config(text="Power: Off")
        else:
            self.calc.turn_On()
            self.calc.power_button.config(text="Power: On")
    #Def for asking user if they want to try again or not
#starts the event loop of the GUI application