from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Convertor:
    def __init__(self):

        # Formatting variables
        background_color = "light blue" # can use "#fff00" for example for yellow

        # Convertor Frame
        self.convertor_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.convertor_frame.grid()

        #Temperature Convertor Heading (row 0)
        self.temp_heading_label = Label(self.convertor_frame,
                                        text = "Temperature Converter",
                                        font="Arial 16 bold", # it's the same as the form where the each terms 
                                                              #are separted in different brackets
                                        bg=background_color,
                                        padx=10,pady=10)
        self.temp_heading_label.grid(row=0)

        # User instrutions (row 1)
        self.temp_instructions_label = Label(self.convertor_frame,
                                             text="Type in the amount to be"
                                             "converted and them push"
                                             "one of the buttons below...",
                                             font="Arial 10 italic", wrap=250,
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
                                  bg="Khaki", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        # second button - convert to fahrenheit button
        # identical code as the first one with some minor changes
        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid", padx=10, pady=10)
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
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)


if __name__== "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()