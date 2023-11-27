import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


data = pd.read_csv('italy-covid-daywise.csv') 

data = data.fillna(0)
data['date'] = pd.to_datetime(data['date'])
monthly_data = data.resample('M', on='date').sum()

def display_totals():
    total_tests = data['new_tests'].sum()
    total_cases = data['new_cases'].sum()
    total_deaths = data['new_deaths'].sum()

    popup = tk.Tk()
    popup.title('Totals')
    popup.configure(bg='green')

    tests_label = tk.Label(popup, text=f"Total Tests: {int(total_tests)}", fg='blue')  
    tests_label.pack()

    cases_label = tk.Label(popup, text=f"Total Cases: {int(total_cases)}", fg='blue')
    cases_label.pack()

    deaths_label = tk.Label(popup, text=f"Total Deaths: {int(total_deaths)}", fg='blue')
    deaths_label.pack()

    popup.geometry("300x150")
    popup.mainloop()

def display_dashboard():
    root = tk.Tk()
    root.title('COVID-19 Dashboard')
    root.geometry("800x600")
    graph_frame = tk.Frame(root)
    graph_frame.pack(fill=tk.BOTH, expand=True)
    fig, axs = plt.subplots(3, 1, figsize=(6, 4), facecolor='green')
    axs[0].bar(monthly_data.index.strftime('%Y-%m'), monthly_data['new_cases'], color='blue')
    axs[0].set_xlabel('Month')
    axs[0].set_ylabel('Total Cases', color='blue')
    axs[0].set_title('Monthly Total Cases', color='blue')
    axs[0].tick_params(axis='x', rotation=45)
    axs[1].bar(monthly_data.index.strftime('%Y-%m'), monthly_data['new_deaths'], color='blue')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Total Deaths', color='blue')
    axs[1].set_title('Monthly Total Deaths', color='blue')
    axs[1].tick_params(axis='x', rotation=45)
    axs[2].bar(monthly_data.index.strftime('%Y-%m'), monthly_data['new_tests'], color='blue')
    axs[2].set_xlabel('Month')
    axs[2].set_ylabel('Total Tests', color='blue')
    axs[2].set_title('Monthly Total Tests', color='blue')
    axs[2].tick_params(axis='x', rotation=45)
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  
    totals_button = tk.Button(root, text="Show Totals", command=display_totals)
    totals_button.pack()

    root.mainloop()
display_dashboard()
