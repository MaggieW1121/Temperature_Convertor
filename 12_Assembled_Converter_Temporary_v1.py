from tkinter import *
from functools import partial # To prevent unwanted windows
import re
from tkmacosx import Button 

import random

class Convertor:
    def __init__(self):

        # Formatting variables
        background_color = "light blue" 

        # Initialise list to hold calculation history
        self.all_calculations = []

        # Convertor Frame
        self.convertor_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.convertor_frame.grid()

        #Temperature Convertor Heading (row 0)
        self.temp_heading_label = Label(self.convertor_frame,
                                        text = "Temperature Converter",
                                        font="Arial 19 bold", # it's the same as the form where the each terms are separted in different brackets
                                        bg=background_color,
                                        padx=10,pady=10)
        self.temp_heading_label.grid(row=0)

        # User instrutions (row 1)
        self.temp_instructions_label = Label(self.convertor_frame,
                                             text="Type in the amount to be"
                                             "converted and them push"
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
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        # second button - convert to fahrenheit button
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
        self.history_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=150,
                                       borderless=1, 
                                       command=lambda: self.history(self.all_calculations))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calculations) == 0:
            self.history_button.configure(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=50,command=self.help, 
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
                answer = "{} °F is {} °C".format(to_convert, celsius)
            
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
            if has_errors != "yes":
                self.all_calculations.append(answer)
                self.history_button.config(state=NORMAL)

        except ValueError:
            self.converted_label.configure(text="Please enter a number", fg="red")
            self.to_convert_entry.configure(bg=error)
   
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded
    
    def history(self, calc_history):
        History(self, calc_history)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box "
                                     "and then push one of the buttons to convert the number "
                                     "to either °C or °F.\n\n" 
                                     "The Calculation History area shows up to seven "
                                     "past calculations (most recent at the top).\n\n"
                                     "You can also export your full calculation history "
                                     "to a text file if desired.") # Use \n to insert line breaks. Two line breaks will give a new paragraph

class History:
    def __init__(self, partner, calc_history):

        background = "LightCyan2"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Set up child window (i.e. history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', 
                                  partial(self.close_history, partner))

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
                
        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation history. "
                                         "You can use the export button to "
                                         "save this data to a text file if desired")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                       bg=background, font="Arial 12", justify = LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text= "Export",
                                    font="Arial 12 bold", borderless=1, 
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text = "Dismiss", borderless=1,
                                     font=("Arial", "12", "bold"),
                                    command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)
    
    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)

        background = "LightCyan2"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Set up child window (i.e. export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', 
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width = 300, bg=background)
        self.export_frame.grid()

        # Set up Export heading - row 0
        self.exp_heading = Label(self.export_frame, 
                                 text="Export / Instructions",
                                 font=("Arial", "14", "bold"), bg=background)
        self.exp_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame,
                                  text="Enter a filename in the box below "
                                  "and press the Save button to save your "
                                  "calculation history to a text file. ",
                                  wrap = 250,
                                  justify=LEFT, width=40, bg=background)
        self.export_text.grid(row=1)

        # Export text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists."
                                 "It's contents will be replaced with your calculation history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10)
        self.export_text.grid(row=2, pady=10)

        # File Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, borderless=1, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", borderless=1,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == "":
                problem = "(No spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
             # Display error message
             self.save_error_label.config(text="Invalid filename - {}".format(problem))
             # Change entry box background to pink
             self.filename_entry.config(bg="#ffafaf")
             print()

        else:
             # If there are no errors, generate text file and then close dialogue
             # add .txt suffix!
             filename = filename + ".txt"

             # create file to hold data
             f = open(filename, "w+")

             # add new line at end of each item
             for item in calc_history:
                 f.write(item + "\n")

             # close file
             f.close()

             # close dialogue
             self.close_export(partner)
    
    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

class Help:
    def __init__(self, partner):

        background = "LightCyan2" 

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (i.e. history box)
        self.help_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.help_box.protocol('WM_DELETE_WINDOW', 
                                  partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width = 300, bg=background)
        self.help_frame.grid()

        # Set up Help heading - row 0
        self.help_heading = Label(self.help_frame, 
                                 text="Help",
                                 font=("Arial", "14", "bold"), bg=background)
        self.help_heading.grid(row=0)

        # Instructions (label, row 1)
        self.help_text = Label(self.help_frame,
                                  text="Enter a filename in the box below "
                                  "and press the Save button to save your "
                                  "calculation history to a text file. ",
                                  wrap = 250,
                                  justify=LEFT, width=40, bg=background)
        self.help_text.grid(row=1)

        # Save / Cancel Frame (row 4)
        self.cancel_frame = Frame(self.help_frame)
        self.cancel_frame.grid(row=5, pady=10)

        self.cancel_button = Button(self.cancel_frame, text="Cancel", borderless=1,
                                    command=partial(self.close_help, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_help(self, partner):
        # Put export button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__== "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()