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
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    # When the user press the button, it will show that the user has asked for help
    def help(self):
        print(" You have successfully asked for help")
        # envoke the help class
        get_help = Help(self)
        # edit the label in the class
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):

        background = "orange"

        # Set up child window (i.e. help box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()


        # Set up Help heading - row 0
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font=("Arial", "10", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        # Dismiss button - row 2
        self.dismiss_button = Button(self.help_frame, text = "Dismiss", width=10, 
                                     bg="orange", font=("Arial", "10", "bold"),
                                     command=self.close_help)
        self.dismiss_button.grid(row=2, pady=10)
    
    def close_help(self):
        self.help_box.destroy()

# main routine
if __name__== "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()

    
