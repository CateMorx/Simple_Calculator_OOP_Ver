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
            #ensures that num1 and num2 is an integer and has a value
            if not isinstance(num_1, int):
                raise TypeError
            elif not num_1:
                raise ValueError
            elif not isinstance(num_2, int):
                raise TypeError
            elif not num_2:
                raise ValueError
            #Prints error message for corresponding type of Error
        except TypeError:
            messagebox.showerror("TypeError", "Number 1 must be an integer")
        except ValueError:
            messagebox.showerror("ValueError", "Number 1 must be an integer")
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
            elif not num_1:
                raise ValueError
            elif not isinstance(num_2, int):
                raise TypeError
            elif not num_2:
                raise ValueError
            #Prints error message for corresponding type of Error
        except TypeError:
            messagebox.showerror("TypeError", "Number 1 must be an integer")
        except ValueError:
            messagebox.showerror("ValueError", "Number 1 must be an integer")
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
            elif not num_1:
                raise ValueError
            elif not isinstance(num_2, int):
                raise TypeError
            elif not num_2:
                raise ValueError
            #Prints error message for corresponding type of Error
        except TypeError:
            messagebox.showerror("TypeError", "Number 1 must be an integer")
        except ValueError:
            messagebox.showerror("ValueError", "Number 1 must be an integer")
        else:
            result = self.num_1 * self.num_2
            self.result=result
            return
    # def for performing the division operation 
    def operation_division(self,num_1,num_2):
        try:
            #ensures that num1 and num2 is an integer and has a value
            if not isinstance(num_1, int):
                raise TypeError
            elif not num_1:
                raise ValueError
            elif not isinstance(num_2, int):
                raise TypeError
            elif not num_2:
                raise ValueError
            #Prints error message for corresponding type of Error
        except TypeError:
            messagebox.showerror("TypeError", "Number 1 must be an integer")
        except ValueError:
            messagebox.showerror("ValueError", "Number 1 must be an integer")
        else:
            result = self.num_1/ self.num_2
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
    def get_results(self):
        return self.result
    def get_num1(self):
        return self.num_1
    def get_num2(self):
        return self.num_2
