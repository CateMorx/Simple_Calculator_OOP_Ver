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
        options = ["1-Additon", "2-Subtraction", "3-Multiplication", "4-Division"]
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
#Def for button functions
    #def for power button command
    def toggle_power(self):
        if self.calc.on:
            self.calc.turn_Off()
            self.calc.power_button.config(text="Power: Off")
        else:
            self.calc.turn_On()
            self.calc.power_button.config(text="Power: On")

            selected_item = self.calc.combo_model.get()
            self.calc.set_model(selected_item)
            # Create a top-level window for the loading popup
            loading_popup = tkinter.Toplevel()
            loading_popup.title("Initializing...")
            loading_popup.geometry("200x100")
            loading_popup.resizable(False, False)
            
            # Create a label to display the loading message
            label = ttk.Label(loading_popup, text="Initializing " + str(self.calc.get_model()) +  "...", font=("Helvetica", 12))
            label.pack(pady=20)
            
            # Add a progress bar to indicate the loading progress
            progressbar = ttk.Progressbar(loading_popup, mode='determinate')
             # Set the maximum value of the progress bar
            progressbar['maximum'] = 100 
             # Set the minimum value of the progress bar
            progressbar['value'] = 0
            progressbar.pack(pady=10)
            progressbar.start()
            
            # Display the loading popup window
            loading_popup.transient(self.GUI)
            loading_popup.grab_set()
            loading_popup.focus_set()
            delay = 100
            # Close the loading popup after 5 seconds
            while progressbar['value'] < progressbar['maximum']:
                progressbar['value'] += 5
                if progressbar['value'] >= progressbar['maximum']:
                    loading_popup.destroy()
                else:
                    self.GUI.update()
                    self.GUI.after(delay)

    def enter_num1 (self):
        try:
            #Error message when calculator is off and tries to enter number
            if not self.calc.on:
                messagebox.showinfo("Error", "Please turn on the Power")
                return
            num_1 = self.calc.num1_entry.get()
            #Error message if tries to enter a blank number input
            if not num_1:
                messagebox.showinfo("Error", "Please enter a value for Number 1")
                return
            #Raise value error if num1 is not an int
            if not num_1.isdigit():
                raise ValueError

            #sets input as num1
            self.calc.set_num1(int(num_1))
            #confirms there is a number input
            self.num1_calculate=1
        except ValueError:
            messagebox.showerror("ValueError", "Number must be an integer")

    def enter_num2 (self):
        try:
            #Error message when calculator is off and tries to enter number
            if not self.calc.on:
                messagebox.showinfo("Error", "Please turn on the Power")
                return
            num_2 = self.calc.num2_entry.get()
            #Error message if tries to enter a blank number input
            if not num_2:
                messagebox.showinfo("Error", "Please enter a value for Number 2")
                return
            #Raise value error if num2 is not an int
            if not num_2.isdigit():
                raise ValueError

            #sets input as num2
            self.calc.set_num2(int(num_2))
            #confirms there is a number input
            self.num2_calculate=1
        except ValueError:
            messagebox.showerror("ValueError", "Number must be an integer")
 
    def calculate_results(self):
        #Error message when calculator is off and tries to calculate
        if not self.calc.on:
            messagebox.showinfo("Error", "Please turn on the Power")
            return
        #Checks if there is a number input on both num1 and num2
        if self.num1_calculate==0 or self.num2_calculate==0:
            messagebox.showinfo("Error", "Please enter your two numbers first")
            return
        #Shows error message if no operation selected
        if self.calc.selected_option.get() == "Select an operation":
            messagebox.showinfo("Error", "Please select an operation first")
            return
        #Retrieves user's choice
        selected_item = self.calc.combo.get()
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
            if self.calc.get_num2()==0:
                self.calc.operation_division(num_1, num_2)
                self.calc.set_num2(0)
                self.calc.num2_entry.delete(0, tkinter.END)
                return
            else:
                self.calc.operation_division(num_1, num_2)
                results = self.calc.get_results()
                #Clears any previous input in results entry and replaces with current results
                self.calc.results_entry.delete(0, tkinter.END)
                self.calc.results_entry.insert(0, str(results))
        # Asking user if they want to try again or not
        choice = messagebox.askyesno("Try again?", "Do you want to try again?")
        #If no, creates a pop-up Thank you message and closes the program
        if not choice:
            messagebox.showinfo("Thank you message", "Thank you!, You will now proceed to the Scientific Calculator")
            GUI.destroy()
        #If yes, clears all initial input
        else:
            self.calc.num1_entry.delete(0, tkinter.END)
            self.calc.num2_entry.delete(0, tkinter.END)
            self.calc.combo.set("Select an operation")
            self.calc.results_entry.delete(0, tkinter.END)
            self.num1_calculate=0
            self.num2_calculate=0

#starts the event loop of the GUI application
GUI = tkinter.Tk()
GUI.title("Calculator")
GUI_calculator= calculator_GUI(calc, GUI)
GUI.mainloop()