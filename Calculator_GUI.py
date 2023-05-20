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
    #Def for button functions
    #Def fo asking user if they want to try again or not
#starts the event loop of the GUI application