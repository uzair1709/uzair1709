import tkinter as tk

def evaluate_expression(event=None):
    try:
        result = eval(entry_field.get())
        entry_field.insert(tk.END,str(result))
    except Exception as e:
        entry_field.insert(tk.END,("Error"))

root = tk.Tk()
root["bg"]="white"
root.title("Calculator")

# Entry field
entry_field = tk.Entry(root, width=60)
entry_field.grid(row=0, column=0, columnspan=4)

# First row buttons
button_7 = tk.Button(root, text="7",height=5,width=8,bg="grey",font=("100"),command=lambda: entry_field.insert(tk.END, "7"))
button_7.grid(row=1, column=0)
button_8 = tk.Button(root, text="8",height=5,width=8,bg="grey",font=("100"),command=lambda: entry_field.insert(tk.END, "8"))
button_8.grid(row=1, column=1)
button_9 = tk.Button(root, text="9",height=5,width=8,bg="grey",font=("100"),command=lambda: entry_field.insert(tk.END, "9"))
button_9.grid(row=1, column=2)
button_divide = tk.Button(root, text="/",height=5,width=8,bg="grey",font=("100"), command=lambda: entry_field.insert(tk.END, "/"))
button_divide.grid(row=1, column=3)
# Second row buttons
button_4 = tk.Button(root, text="4",height=5,width=8,bg="grey", font=("100"),command=lambda: entry_field.insert(tk.END, "4"))
button_4.grid(row=2, column=0)
button_5 = tk.Button(root, text="5",height=5,width=8,bg="grey", font=("100"),command=lambda: entry_field.insert(tk.END, "5"))
button_5.grid(row=2, column=1)
button_6 = tk.Button(root, text="6",height=5,width=8 ,bg="grey",font=("100"),command=lambda: entry_field.insert(tk.END, "6"))
button_6.grid(row=2, column=2)
button_multiply = tk.Button(root, text="*",height=5,width=8,bg="#330D6D",font=("100"), command=lambda: entry_field.insert(tk.END, ""))
button_multiply.grid(row=2, column=3)

# Third row buttons
button_1 = tk.Button(root, text="1",height=5,width=8,bg="#695D6C", font=("100"),command=lambda: entry_field.insert(tk.END, "1"))
button_1.grid(row=3, column=0)
button_subtraction = tk.Button(root, text="-",height=5,width=8,bg="#695D6C",font=("100"), command=lambda: entry_field.insert(tk.END, "-"))
button_subtraction.grid(row=3, column=1)
button_2 = tk.Button(root, text="2",height=5,width=8,  bg="#695D6C",font=("100"),command=lambda: entry_field.insert(tk.END, "2"))
button_2.grid(row=3, column=2)
button_addition = tk.Button(root, text="+",height=5,width=8,bg="#695D6C", font=("100"), command=lambda: entry_field.insert(tk.END, "+"))
button_addition.grid(row=3, column=3)
# Fourth row buttons
button_0 = tk.Button(root, text="0",height=5,width=8,bg="#695D6C",font=("100"),  command=lambda: entry_field.insert(tk.END, "0"))
button_0.grid(row=4, column=0)
button_dot = tk.Button(root, text=".",height=5,width=8,bg="#695D6C", font=("100"), command=lambda: entry_field.insert(tk.END, "."))
button_dot.grid(row=4, column=1)
button_equalsto = tk.Button(root, text="=",height=5,width=8,bg="#695D6C",font=("100"),  command=evaluate_expression)
button_equalsto.grid(row=4, column=2)
button_clear = tk.Button(root, text="C",height=5,width=8,bg="#695D6C",font=("100"),command=lambda: entry_field.delete(0, tk.END))
button_clear.grid(row=4, column=3)

# Bind the Enter key to the evaluate_expression function
root.bind('<Return>', evaluate_expression)

root.mainloop()