import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def update_task():
    try:
        selected_task = task_listbox.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def complete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task, {'bg': 'light green'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and configure widgets
task_entry = tk.Entry(root, width=30)
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
complete_button = tk.Button(root, text="Mark as Completed", command=complete_task)

# Place widgets on the grid
task_entry.grid(row=0, column=0, columnspan=2)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10)
add_button.grid(row=0, column=2)
remove_button.grid(row=1, column=2)
update_button.grid(row=2, column=2)
complete_button.grid(row=3, column=2)

root.mainloop()
