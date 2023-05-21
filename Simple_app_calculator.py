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
        self.model=""
    #Creates def for on and off of calculator
    def turn_On(self):
        self.on = True

    def turn_Off(self):
        self.on = False
     # def for performing the addition operation 
    def operation_addition(self,num_1,num_2):
        try:
            #ensures that num1 and num2 is an integer and has a value
            if not isinstance(num_1, int):
                raise TypeError
            elif not isinstance(num_2, int):
                raise TypeError
            #Prints error message for corresponding type of Error
        except TypeError:
            messagebox.showerror("TypeError", "Number 1 must be an integer")
        else:
            result = self.num_1 + self.num_2
            self.result=result
            return
    # def for performing the subtraction operation 
    def operation_subtraction(self,num_1,num_2):
        try:
            #ensures that num1 and num2 is an integer and has a value
            if not isinstance(num_1, int):
                raise TypeError
            elif not isinstance(num_2, int):
                raise TypeError
            #Prints error message for corresponding type of Error
        except TypeError:
            messagebox.showerror("TypeError", "Number 1 must be an integer")
        else:
            result = self.num_1 - self.num_2
            self.result=result
            return
    # def for performing the multiplication operation 
    def operation_multiplication(self,num_1,num_2):
        try:
            #ensures that num1 and num2 is an integer and has a value
            if not isinstance(num_1, int):
                raise TypeError
            elif not isinstance(num_2, int):
                raise TypeError
            #Prints error message for corresponding type of Error
        except TypeError:
            messagebox.showerror("TypeError", "Number 1 must be an integer")
        else:
            result = self.num_1 * self.num_2
            self.result=result
            return
    # def for performing the division operation 
    def operation_division(self,num_1,num_2):
        try:
            if not isinstance(num_1, int):
                 raise TypeError
            elif not isinstance(num_2, int):
                 raise TypeError
            elif num_2==0:
                self.result="Error"
                raise ValueError
        except TypeError:
            messagebox.showerror("TypeError", "Number must be an integer")
            return
        except ValueError:
            messagebox.showerror("Value Error", "Value of number 2 must not be equal to 0")
            return
        else:
            result = self.num_1/self.num_2
            self.result=result
            return
    #Creates def for Input of num1 & num2
    def set_num1(self, num_1):
        try:
            if not isinstance(num_1, int):
                raise TypeError
        except TypeError:
            messagebox.showerror("TypeError", "Number must be an integer")
        else:
            self.num_1 = num_1
            return self.num_1

    def set_num2(self, num_2):
        try:
            if not isinstance(num_2, int):
                raise TypeError
        except TypeError:
            messagebox.showerror("TypeError", "Number must be an integer")
        else:
            self.num_2 = num_2
            return self.num_2
    def set_model(self, model):
        if model[0] == '1':
            model ="Casio"
            self.model=model
        elif model[0] == '2':
            model ="Samsung"
            self.model=model
        if model[0] == '3':
            model ="Sony"
            self.model=model
        return
    def get_model(self):
        return self.model
    def get_results(self):
        return self.result
    def get_num1(self):
        return self.num_1
    def get_num2(self):
        return self.num_2
