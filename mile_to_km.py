from tkinter import *

def mile_to_km():
    """
    Convert miles to kilometers and update the kilometer result label.
    """
    miles = float(miles_input.get())  # Get the value from the input field and convert it to a float
    km = miles * 1.609  # Convert miles to kilometers
    kilometer_result_label.config(text=f"{km:.2f}")  # Update the result label with the converted value

# Initialize the main application window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Create an entry widget for inputting miles
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Create a label for the miles input
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Create a label for "is equal to"
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Create a label to display the result in kilometers
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Create a label for "Km"
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Create a button that triggers the conversion when clicked
calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

# Start the Tkinter main event loop
window.mainloop()
