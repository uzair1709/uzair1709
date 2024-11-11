import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    # Get the input from the user
    birth_date_str = entry_birth_date.get()
    
    try:
        # Convert the input string to a date object
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        today = datetime.today()
        
        # Calculate age
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day
        
        # Display the result
    
        messagebox.showinfo("Age Calculator", f"You are {age_years} years, {age_months} months, and {age_days} days old.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid date in YYYY-MM-DD format.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create a label
label = tk.Label(root, text="Enter your birth date (YYYY-MM-DD):")
label.pack(pady=10)

# Create an entry widget
entry_birth_date = tk.Entry(root)
entry_birth_date.pack(pady=10)

# Create a button to calculate age
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()