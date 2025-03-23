import tkinter as tk
from tkinter import messagebox
from expenses import add_expense, view_expenses, delete_expense, get_monthly_summary


def add_expense_gui():
    """Add expense to the database from GUI input fields."""
    try:
        amount = float(entry_amount.get())
        category = entry_category.get()
        description = entry_desc.get()
        date = entry_date.get()

        if not amount or not category or not date:
            label_status.config(text="Please fill all required fields!", fg="red")
            return

        add_expense(amount, category, description, date)
        label_status.config(text="Expense Added Successfully!", fg="green")

        # Clear input fields after adding
        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
        entry_date.delete(0, tk.END)

        view_expenses_gui()  # Refresh the expense list

    except ValueError:
        label_status.config(text="Invalid amount! Please enter a number.", fg="red")


def view_expenses_gui():
    """Fetch and display expenses in the listbox."""
    expenses = view_expenses()
    expense_list.delete(0, tk.END)  # Clear list before updating
    if not expenses:
        expense_list.insert(tk.END, "No expenses found.")
    else:
        for expense in expenses:
            expense_list.insert(tk.END, f"ID: {expense[0]} | Amount: ${expense[1]:.2f} | Category: {expense[2]} | Description: {expense[3]} | Date: {expense[4]}")


def delete_expense_gui():
    """Delete selected expense from the database."""
    try:
        selected_item = expense_list.get(expense_list.curselection())  # Get selected item
        expense_id = selected_item.split(" | ")[0].split(": ")[1]  # Extract ID
        delete_expense(expense_id)
        messagebox.showinfo("Success", "Expense Deleted Successfully!")
        view_expenses_gui()  # Refresh the list
    except:
        messagebox.showerror("Error", "Please select an expense to delete.")


def show_monthly_summary():
    """Show the total expenses for the selected month."""
    month = entry_month.get()
    if not month:
        messagebox.showerror("Error", "Please enter a month (YYYY-MM)")
        return

    total = get_monthly_summary(month)
    label_summary.config(text=f"Total Expenses for {month}: ${total:.2f}", fg="blue")


# Create the main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x600")  # Increased height to accommodate the monthly summary section
root.configure(bg="#f0f0f0")  # Light gray background

# Frame for input fields
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

# Labels and Entry Fields
tk.Label(input_frame, text="Amount:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_amount = tk.Entry(input_frame, font=("Arial", 10))
entry_amount.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Category:", bg="#f0f0f0", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_category = tk.Entry(input_frame, font=("Arial", 10))
entry_category.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Description:", bg="#f0f0f0", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_desc = tk.Entry(input_frame, font=("Arial", 10))
entry_desc.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Date (YYYY-MM-DD):", bg="#f0f0f0", font=("Arial", 10)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_date = tk.Entry(input_frame, font=("Arial", 10))
entry_date.grid(row=3, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Expense", command=add_expense_gui, bg="#4CAF50", fg="white", font=("Arial", 10)).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="View Expenses", command=view_expenses_gui, bg="#2196F3", fg="white", font=("Arial", 10)).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Selected Expense", command=delete_expense_gui, bg="#f44336", fg="white", font=("Arial", 10)).grid(row=0, column=2, padx=5)

# Listbox to show expenses
expense_list = tk.Listbox(root, width=70, height=10, font=("Arial", 10))
expense_list.pack(pady=10)

# Status Label
label_status = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 10))
label_status.pack()

# Monthly Summary Section
summary_frame = tk.Frame(root, bg="#f0f0f0")
summary_frame.pack(pady=10)

tk.Label(summary_frame, text="Enter Month (YYYY-MM):", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_month = tk.Entry(summary_frame, font=("Arial", 10))
entry_month.grid(row=0, column=1, padx=5, pady=5)

tk.Button(summary_frame, text="Show Summary", command=show_monthly_summary, bg="#17a2b8", fg="white", font=("Arial", 10)).grid(row=0, column=2, padx=5)

label_summary = tk.Label(summary_frame, text="", bg="#f0f0f0", font=("Arial", 10))
label_summary.grid(row=1, column=0, columnspan=3, pady=5)

# Initial view of expenses
view_expenses_gui()
