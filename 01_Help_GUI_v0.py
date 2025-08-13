from tkinter import *

import random

class Convertor:
    def __init__(self, parent):
        
        # Formatting variables...
        background_color = "light blue"

        # Cinvertor Main Screen GUI...
        self.convertor_frame = Frame(width=600, height= 600, bg=background_color,
                                     pady=10) # apply padding to the convertor frame
        self.convertor_frame.grid()

        # Temperature Convertor Heading (row 0)
        self.temp_convertor_label = Label(self.convertor_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.convertor_frame, text="help", 
                                  font=("Arial", "14"),
                                  padx=10, pady=10)
        self.help_button.grid(row=1)

# main routine
if __name__== "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()