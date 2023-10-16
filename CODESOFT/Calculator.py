import tkinter as tk
from tkinter import ttk

def perform_calculation():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid operation"

    result_label.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Polished Calculator")

# Styling the window
window.geometry("400x350")
window.configure(bg="#f2f2f2")

# Title label
title_label = tk.Label(window, text="Calculator", font=("Helvetica", 20, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)

# Number entry fields with labels
label_num1 = tk.Label(window, text="Enter first number:", font=("Helvetica", 12), bg="#f2f2f2")
label_num1.pack()
entry_num1 = tk.Entry(window, font=("Helvetica", 12))
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter second number:", font=("Helvetica", 12), bg="#f2f2f2")
label_num2.pack()
entry_num2 = tk.Entry(window, font=("Helvetica", 12))
entry_num2.pack()

# Operation dropdown with label
operation_label = tk.Label(window, text="Select Operation:", font=("Helvetica", 12), bg="#f2f2f2")
operation_label.pack()

operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar()
operation_var.set(operations[0])
operation_menu = ttk.Combobox(window, textvariable=operation_var, values=operations, font=("Helvetica", 12))
operation_menu.pack()

# Calculate button with a stylish design
calculate_button = tk.Button(window, text="Calculate", command=perform_calculation, bg="#007acc", fg="white", font=("Helvetica", 12))
calculate_button.pack(pady=10)

# Result label with a bold font
result_label = tk.Label(window, text="Result: ", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
result_label.pack()

# Center the window on the screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_width()) // 2
y = (screen_height - window.winfo_height()) // 2
window.geometry("+{}+{}".format(x, y))

# Start the main loop
window.mainloop()
