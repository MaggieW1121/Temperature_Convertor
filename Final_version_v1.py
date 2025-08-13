import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial # To prevent unwanted windows
import re
from tkmacosx import Button 
import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

import random

class Instruction:
    def __init__(self, root):
        self.root = root

        # Create main frame
        main_frame = Frame(root, padx=20, pady=20)
        main_frame.pack(fill=BOTH, expand=True)

        # Label for instructions
        label = Label(main_frame, text="Please read the instructions below:", font=("Arial", 14))
        label.pack(anchor='w')

        # Frame for scrollable text
        text_frame = Frame(main_frame)
        text_frame.pack(fill=BOTH, expand=True)

        # Scrollbar
        scrollbar = Scrollbar(text_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Text widget with instructions
        self.text = Text(text_frame, height=15, wrap=WORD, yscrollcommand=scrollbar.set)
        self.text.pack(side=LEFT, fill=BOTH, expand=True)

        # Link scrollbar and text
        scrollbar.config(command=self.text.yview)

        # Sample long instruction text
        instruction_text = (
            "Kia ora!\n"
            "Thanks for using this Temperature Convertor!\n\n"
            "Please read the following instructions carefully. They are brief but helpful:\n\n"

            "This convertor contains four main functions, they are:\n"
            "1. Conversion function: \n"
            "This function is to convert temperatures between Centigrade and Fahrenheit. You are allowed to enter a number in the entrybox and then push one of the buttons "
            "to convert the number to either °C or °F.\n"
            "This function will raise a message to double check your input once you entered temperature greater than 10000.\n"
            "Note: This function doesn't accept any temperature lower than -273°C or -459°F, as while at that temperature, "
            "particle motion stops and particles have minimum kinetic energy.\n\n"

            "2. Calculation History function:\n"
            "This function is to show the past calculations (most recent at the top.).\n"
            "You are allowed to choose specific data(s) to plot a trend graph or export it into a text file.\n"
            "You also allowed to choose full calculations or delete any calculation history you don't want.\n\n"

            "3. Plot function:\n"
            "This function is to plot a graph from selected datapoints.\n"
            "You are allowed to select specific datas in your calculation history in any order you like.\n"
            "The graph will plotted in a temperature trend graph. You can export the plot graph for further research.\n\n"

            "4. Export function: \n"
            "This function is to export your full calculation history/some specific datapoints to a text file if desired."
            "If you would like to save the history in an exist file, please enter the full name of your file with .txt (ie. hello_world.txt)\n"
            "Otherwise, you only need to enter the file name you want (ie. hello_world)"
            "\n\n"

            "You are welcome to exit at any time through the dismiss button or the red cross.\n\n"
            "Thanks for reading through everything! Click the continue button to start your journey on temperature conversion!"
        )

        self.text.insert(END, instruction_text)
        self.text.config(state=DISABLED)

        # Continue button (starts disabled with countdown)
        self.continue_button = Button(main_frame, text="Continue (20)", state=DISABLED, 
                                      command=self.continue_pressed)
        self.continue_button.pack(pady=10)

        # Start the countdown
        self.countdown(30)

    def countdown(self, seconds):
        if seconds > 0:
            self.continue_button.config(text=f"Continue ({seconds})", state=DISABLED)
            self.root.after(1000, self.countdown, seconds - 1)  # Update every second
        else:
            self.continue_button.config(text="Continue", state=NORMAL)

    def continue_pressed(self):
        self.root.destroy()  # Close instructions
        Convertor() # Open the converter window

class Convertor:
    def __init__(self):

        # Formatting variables
        background_color = "light blue" 

        # Initialise list to hold calculation history
        self.all_calculations = []

        # Set up the title for the Convertor GUI
        self.root = Tk()
        self.root.title("Temperature Convertor")

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
                                             "converted and them push "
                                             "one of the buttons below...",
                                             font="Arial 12 italic", wrap=290,
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
        error = "#ffafaf"  # Pale pink background for errors
        
        # Retrieve amount into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check for extreme values
            if to_convert > 10000:
                response = messagebox.askyesno("Extreme Temperature Warning",
                                            f"You entered {to_convert}.\n"
                                            "Are you sure you want to continue?")
                if not response:
                    self.to_convert_entry.delete(0, END)
                    self.to_convert_entry.config(bg=error)
                    self.converted_label.config(text="Typo! Entry box cleared.", fg="red")
                    return

            # Determine direction of conversion using low as a flag
            if low == -273 and to_convert >= low:  # Convert from Celsius to Fahrenheit
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = f"{to_convert} °C is {fahrenheit} °F"
                self.to_convert_entry.delete(0, END)

            elif low == -459 and to_convert >= low:  # Convert from Fahrenheit to Celsius
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = f"{to_convert} °F is {celsius} °C"
                self.to_convert_entry.delete(0, END)

            else:
                answer = "You have exceeded the lowest possible temperature!\n\n" \
                "Please enter numbers larger than -273°C or -459°F"
                has_errors = "yes"
                self.to_convert_entry.delete(0, END)

            # Display the result
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Save to history if valid
            if has_errors != "yes":
                self.all_calculations.append(answer)
                self.history_button.configure(state=NORMAL)

        except ValueError:
            self.converted_label.configure(text="Please enter a number", fg="red")
            self.to_convert_entry.configure(bg=error)
            self.to_convert_entry.delete(0, END)
   
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded
    
    def history(self, calculation_history):
        History(self, calculation_history)

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

        # Create a list which store selected calculations for trend graph
        self.selected_calculations = []

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
                                  text="Here are your recent calculations. "
                                  "Select history calculations to generate trend graph or export:\n\n",
                                  wrap = 250, font = "arial 12 italic",
                                  justify=LEFT, width=40, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        self.history_list = Listbox(self.history_frame, height = 10,
                                    width=40, selectmode = MULTIPLE) # the code "selectmode = MULTIPLE" is to allow the user to choose multiple choices among all the calculation historys displayed
        self.history_list.grid(row=2, padx = 10)

        for item in reversed(calc_history):
            self.history_list.insert(END, item)

        # Select All Button Frame (row 3)
        self.select_button_frame = Frame(self.history_frame)
        self.select_button_frame.grid(row=3, pady=10)

        # Select All Button
        self.select_all_button = Button(self.select_button_frame, text="Select All",
                                        font="Arial 10 bold", command=self.select_entries)
        self.select_all_button.grid(row=0, column=0)

        # Unselect All Button
        self.unselect_button = Button(self.select_button_frame, text="Unselect All",
                                      font="Arial 10 bold", command=self.unselect_entries)
        self.unselect_button.grid(row=0, column=1, padx=5)

        # Trend Graph Button Frame (row 4)
        #self.trend_graph_button_frame = Frame(self.history_frame)
        #self.trend_graph_button_frame.grid(row=4, pady=10)

        # Generate Trend Graph Button
        #self.trend_button = Button(self.trend_graph_button_frame, text="Generate Trend Graph",
                                   #font="Arial 12 bold", borderless=1, 
                                   #command= self.generate_trend_graph)
        #self.trend_button.grid(row=0,column=0)

        # Export / Dismiss Buttons Frame (row 5)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=5, pady=10)

        # Generate Trend Graph Button
        self.trend_button = Button(self.export_dismiss_frame, text="Generate Trend Graph",
                                   font="Arial 12 bold", borderless=1, 
                                   command= self.generate_trend_graph)
        self.trend_button.grid(row=0,column=0)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text= "Export",
                                    font="Arial 12 bold", borderless=1, 
                                    command=lambda: self.export_selected(calc_history))
        self.export_button.grid(row=0, column=1)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text = "Dismiss", borderless=1,
                                     font=("Arial", "12", "bold"),
                                    command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=2)

    def select_entries(self):
        self.history_list.select_set(0, END)

    def unselect_entries(self):
        self.history_list.select_clear(0, END)

    def export_selected(self, calc_history):
        selected_indices = self.history_list.curselection()
        if not selected_indices:
            messagebox.showwarning("Warning", f"You haven't selected any data yet!")
            return

        count = len(selected_indices)
        confirm = messagebox.askyesno("Confirm Export", 
                                       f"You have selected {count} data point(s). Do you want to continue?")
        if not confirm:
            self.history_list.select_clear(0, END)
            return

        actual_indices = [len(calc_history) - 1 - idx for idx in selected_indices]
        selected_calcs = [calc_history[idx] for idx in actual_indices]

        Export(self, selected_calcs)  

    def generate_trend_graph(self):
        selected_indices = self.history_list.curselection()
        if not selected_indices:
            messagebox.showwarning("Warning", f"You haven't selected any data yet!")
            return
        
        # Extract temperature values from selected entries
        temperatures = []
        for idx in selected_indices:
            entry = self.history_list.get(idx)
            # Extract numeric value from the entry string
            try:
                # Look for the first number in the string
                value_str = re.search(r'[-+]?\d*\.\d+|\d+', entry).group()
                temperatures.append(float(value_str))
            except (AttributeError, ValueError):
                continue
        
        if not temperatures:
            return
        
        # Create a new window for the graph
        graph_window = Toplevel(self.history_box)
        graph_window.title("Temperature Trend")
        
        # Create a figure
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(temperatures, marker='o', linestyle='-')
        ax.set_title("Temperature Conversion Trend")
        ax.set_xlabel("Conversion Sequence")
        ax.set_ylabel("Temperature Value")
        ax.grid(True)

        # Embed the plot in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, graph_window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)

        canvas.mpl_connect("key_press_event", on_key_press)
        
        # Add a close button
        close_btn = Button(graph_window, text="Close", borderless=1,
                           command=graph_window.destroy)
        close_btn.pack(pady=10)
    
    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

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
                                 "Its contents will be replaced with your calculation history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 12 italic", wrap=225, padx=10)
        self.export_text.grid(row=2, pady=10)

        # File Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Timestamp suggestion
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.timestamp_label = Label(self.export_frame, 
                                     text=f"Suggested: history_{current_time}.txt",
                                     font="Arial 14 italic", bg=background)
        self.timestamp_label.grid(row=4, pady=5)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=5)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=6, pady=10)


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

        # If filename is empty, use timestamp
        if filename == "":
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"history_{current_time}"
        else:
            # Validate filename
            for letter in filename:
                if re.match(valid_char, letter):
                    continue
                elif letter == " ":
                    problem = "(No spaces allowed)"
                else:
                    problem = f"(no '{letter}' allowed)"
                has_error = "yes"
                break

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text=f"Invalid filename - {problem}")
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            return

        # Add .txt suffix if not present
        if not filename.endswith(".txt"):
            filename += ".txt"

        # Check if file exists
        if os.path.exists(filename):
            confirm_overwrite = messagebox.askyesno("File Already Exists",
                            f"The file '{filename}' already exists.\nDo you want to overwrite it?")
            if not confirm_overwrite:
                self.save_error_label.config(text="Export cancelled by user.", fg="maroon")
                return

        # Create file to hold data
        try:
            with open(filename, "w") as f:
                f.write("Temperature Conversion History\n")
                f.write("=" * 40 + "\n")
                for i, item in enumerate(calc_history, 1):
                    f.write(f"{i}. {item}\n")
            
            # Show success message
            self.save_error_label.config(text=f"Success! Saved to {filename}", fg="green")
            self.filename_entry.config(bg="white")

            # Change button to close
            self.save_button.config(text="Close", 
                                   command=partial(self.close_export, partner))
            self.cancel_button.grid_forget()
            
        except Exception as e:
            self.save_error_label.config(text=f"Error: {str(e)}", fg="red")
    
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
    something = Instruction(root)
    root.mainloop()