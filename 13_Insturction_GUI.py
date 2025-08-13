from tkinter import *
from tkinter import ttk

class InstructionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Instructions")

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

            "2. Plot function:\n"
            "This function is to plot a graph from selected datapoints.\n"
            "You are allowed to select specific datas in your calculation history in any order you like.\n"
            "The graph will plotted in a temperature trend graph. You can export the plot graph for further research.\n\n"

            "3. Export function: \n"
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
        self.continue_button = Button(main_frame, text="Continue (20)", state=DISABLED, command=self.continue_pressed)
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
        print("Continue button pressed!")
        self.root.destroy()

# Run the app
if __name__ == "__main__":
    root = Tk()
    app = InstructionApp(root)
    root.mainloop()