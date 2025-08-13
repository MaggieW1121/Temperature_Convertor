# this version is to make some changes base on what I have done in "01_Help_GUI_v3"
# Skill learned:
# CamelCase: each word starts with an uppercase character but there are no spaces
# e.g. class name need to start with capital letter

from tkinter import *
from functools import partial # To prevent unwanted windows

import random

class Convertor:
    def __init__(self):
        
        # Formatting variables...
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations
        self.all_calculations = ['0 °F is -17.8 °C', 
                                 '10 °F is -12.2 °C', 
                                 '40 °F is 4.4 °C', 
                                 '20 °F is -6.7 °C', 
                                 '12 °F is -11.1 °C', 
                                 '24 °F is -4.4 °C', 
                                 '100 °F is 37.8 °C']

        # Convertor Main Screen GUI...
        self.convertor_frame = Frame(width=300, height= 300, bg=background_color,
                                     pady=10) # apply padding to the convertor frame
        self.convertor_frame.grid()

        # Temperature Convertor Heading (row 0)
        self.temp_convertor_label = Label(self.convertor_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # History Button (row 1)
        self.history_button = Button(self.convertor_frame, text="history", 
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=lambda: self.history(self.all_calculations))  # change from equal to lambda
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):

        background = "LightCyan2"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Set up child window (i.e. history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width = 300, bg=background)
        self.history_frame.grid()

        # Set up history heading - row 0
        self.his_heading = Label(self.history_frame, text="Calculation History",
                                 font=("Arial", "19", "bold"), bg=background)
        self.his_heading.grid(row=0)

        # History text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent calculations. "
                                  "Please use the export button to create a text file "
                                  "of all your calculations for this session. ",
                                  wrap = 250, font = "arial 10 italic",
                                  justify=LEFT, width=40, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here.. (row 2)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                                      - item - 1]+"\n" 
                #history_string += calc_history(len(calc_history)
                                                      #- item - 1)+"\n" 

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                       bg=background, font="Arial 12", justify = LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text= "Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text = "Dismiss", width=10, 
                                     font=("Arial", "12", "bold"),
                                    command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)
    
    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__== "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()