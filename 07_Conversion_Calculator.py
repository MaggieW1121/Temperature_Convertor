from tkinter import *
from tkmacosx import Button 
from functools import partial  # To prevent unwanted windows
import random


class Convertor:
    def __init__(self):

        # Formatting variables
        background_color = "light blue" 

        # Convertor Frame
        self.convertor_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.convertor_frame.grid()

        #Temperature Convertor Heading (row 0)
        self.temp_heading_label = Label(self.convertor_frame,
                                        text = "Temperature Converter",
                                        font="Arial 19 bold", 
                                        bg=background_color,
                                        padx=10,pady=10)
        self.temp_heading_label.grid(row=0)

        # User instrutions (row 1)
        self.temp_instructions_label = Label(self.convertor_frame,
                                             text="Type in the temperature to be"
                                             "converted and then push"
                                             "one of the buttons below...",
                                             font="Arial 10 italic", wrap=290,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temoerature entry box (row 2)
        self.to_convert_entry = Entry(self.convertor_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.convertor_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        # first button - convert to centigrade button
        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="Khaki", padx=10, pady=10,
                                  borderless=1,
                                  command=lambda: self.temp_convert(-459)) #minimum value that is valid, which means the minimum is -459
        self.to_c_button.grid(row=0, column=0)

        # second button - convert to fahrenheit button
        # identical code as the first one with some minor changes
        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid", padx=10, pady=10, 
                                  borderless=1,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer lavel (row 4)
        self.converted_label = Label(self.convertor_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color, pady=10, 
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)
        
        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.convertor_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        # two buttons for history
        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=150,
                                       borderless=1)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=50,
                                  borderless=1)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf" # Pale pink background for when entry box has errors

        # Retrieve amount into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check and convert to Fahrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} °C is {} °F".format(to_convert, fahrenheit)

            # Check and convert to Centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} °C is {} °F".format(to_convert, celsius)

            else:
                # Input is invalid (Too Cold!)
                answer = "Too Cold!"
                has_errors = "yes"

            # Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)
            # Add answer to list for history

        except ValueError:
            self.converted_label.configure(text="Please enter a number", fg="red")
            self.to_convert_entry.configure(bg=error)
   
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded    

if __name__== "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()