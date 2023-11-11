import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

app = tk.Tk()
app.title("Expense Tracker")
app.geometry("800x800")

# Database
expenses = []

def app_exp():
    exp = {
        "date": datetime.now(),
        "category": category_entry.get(),
        "amount": float(amount_entry.get()),
        'description': description_entry.get()
    }
    expenses.append(exp)
    update_expense_list()
    update_total_label() 
    clear_entries()

#clearing entries
def clear_entries():
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

#for the list to be updated
def update_expense_list():
    expense_list.delete(0, tk.END)
    for expense in expenses:
        expense_list.insert(tk.END, f"{expense['date']} - {expense['category']} - ${expense['amount']} - {expense['description']}")

#fun for the total
def update_total_label():
    total_amount = sum(expense['amount'] for expense in expenses)
    total_label.config(text=f"Total Expenses: ${total_amount:.2f}")

#visual
def gen_final_report():
    monthly_report = gen_mon_report(pd.DataFrame(expenses))

    if not monthly_report.empty:
        # Plotting a bar graph
        monthly_report.plot(kind='bar')
        plt.xlabel('Month-Year')
        plt.ylabel('Total Expenses ($)')
        plt.title('Monthly Expense Report')
        plt.show()
    else:
        messagebox.showinfo("Report", "No data for the report.")

#groupoing
def gen_mon_report(expenses_df):
    monthly_periods = expenses_df['date'].dt.to_period("M")

    # Group the DataFrame by month-year periods and calculate the sum of 'amount'
    monthly_grouped = expenses_df.groupby(monthly_periods)['amount'].sum()

    # Return the resulting Series
    return monthly_grouped


#basically this the entry for catagory
category_label = tk.Label(app, text="Category:")
category_label.pack()
category_entry = tk.Entry(app)
category_entry.pack()
#amount
amount_label = tk.Label(app, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(app)
amount_entry.pack()
#discription 
description_label = tk.Label(app, text="Description:")
description_label.pack()
description_entry = tk.Entry(app)
description_entry.pack()
#botton wigdt gen
add_button = tk.Button(app, text="Add Expense", command=app_exp)
add_button.pack()

generate_button = tk.Button(app, text="Generate Report", command=gen_final_report)
generate_button.pack()
#for the final list 
expense_list = tk.Listbox(app, height=10, width=100)
expense_list.pack()

#total expenses
total_label = tk.Label(app, text="Total Expenses: rs-0.00")
total_label.pack()

app.mainloop()
