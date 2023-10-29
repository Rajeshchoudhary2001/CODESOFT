import tkinter as tk
from tkinter import messagebox

# Create an empty contact list
contacts = []

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        contacts.append(contact)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and phone are required!")

# Function to view all contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact['Name'] + " - " + contact['Phone'])

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            contact_list.insert(tk.END, contact['Name'] + " - " + contact['Phone'])

# Function to update a contact
def update_selected_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    for contact in contacts:
        if selected_contact in contact['Name'] + " - " + contact['Phone']:
            name_entry.delete(0, tk.END)
            name_entry.insert(tk.END, contact['Name'])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(tk.END, contact['Phone'])
            email_entry.delete(0, tk.END)
            email_entry.insert(tk.END, contact['Email'])
            address_entry.delete(0, tk.END)
            address_entry.insert(tk.END, contact['Address'])
            break

# Function to delete a contact
def delete_selected_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    for contact in contacts:
        if selected_contact in contact['Name'] + " - " + contact['Phone']:
            contacts.remove(contact)
            update_contact_list()
            clear_entries()
            break

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Contact Book")

# Create entry fields and labels
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

phone_label = tk.Label(window, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

address_label = tk.Label(window, text="Address:")
address_label.pack()
address_entry = tk.Entry(window)
address_entry.pack()

# Create buttons
add_button = tk.Button(window, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(window, text="Search:")
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

search_button = tk.Button(window, text="Search", command=search_contact)
search_button.pack()

update_button = tk.Button(window, text="Update Selected Contact", command=update_selected_contact)
update_button.pack()

delete_button = tk.Button(window, text="Delete Selected Contact", command=delete_selected_contact)
delete_button.pack()

# Create a listbox to display contacts
contact_list = tk.Listbox(window, selectmode=tk.SINGLE)
contact_list.pack()

# Update the contact list on startup
update_contact_list()

# Start the GUI main loop
window.mainloop()
