import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            result_label.config(text="Password length should be at least 6 characters.")
        else:
            password = generate_password(length)
            result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Please enter a valid number for the password length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and configure widgets
instruction_label = tk.Label(window, text="Enter the desired password length:")
instruction_label.pack(pady=10)

length_entry = tk.Entry(window)
length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

## Center the window on the screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_width()) // 2
y = (screen_height - window.winfo_height()) // 2
window.geometry(f"+{x}+{y}")

# Start the GUI application
window.mainloop()
