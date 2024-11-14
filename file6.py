import tkinter as tk
import time

def update_time():
    """Update the time displayed on the label."""
    current_time = time.strftime('%h:%I:%M:%S %p')  # Get the current time in 12-hour format
    label.config(text=current_time)  # Update the label text
    label.after(1000, update_time)  # Call this function again after 1000 ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")


# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='red', foreground='green')
label.pack(anchor='center')

# Start the time update loop
update_time()

# Start the Tkinter event loop
root.mainloop()