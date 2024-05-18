import tkinter as tk
from tkinter import messagebox

# Function to add expense
def add_expense():
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()
    
    if description and amount and category:
        expenses_listbox.insert(tk.END, f"{description}: ${amount} ({category})")
        description_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please fill out all fields.")

# Function to delete selected expense
def delete_expense():
    selected_item = expenses_listbox.curselection()
    if selected_item:
        expenses_listbox.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "Please select an expense to delete.")

# Create the main application window
root = tk.Tk()
root.title("Expense Tracker")

# Labels
tk.Label(root, text="Description:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Amount ($):").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Category:").grid(row=2, column=0, padx=5, pady=5)

# Entry fields
description_entry = tk.Entry(root, width=30)
description_entry.grid(row=0, column=1, padx=5, pady=5)
amount_entry = tk.Entry(root, width=30)
amount_entry.grid(row=1, column=1, padx=5, pady=5)
category_entry = tk.Entry(root, width=30)
category_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="WE")
delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
delete_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

# Listbox to display expenses
expenses_listbox = tk.Listbox(root, width=50)
expenses_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
