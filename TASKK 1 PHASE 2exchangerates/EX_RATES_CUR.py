import tkinter as tk
from PIL import Image, ImageTk
import requests

BASE_URL = 'https://api.frankfurter.app'

root = tk.Tk()
root.title("Currency Converter")

def per_con():
    amount = float(entry_amount.get())
    from_curr = entry_from_curr.get().upper()
    to_curr = entry_to_curr.get().upper()
    
    response = requests.get(f"{BASE_URL}/latest?amount={amount}&from={from_curr}&to={to_curr}")
    
    if response.status_code == 200:
        data = response.json()
        if 'rates' in data:
            converted_amount = data['rates'][to_curr]
            label_result.config(text=f"{amount} {from_curr} is equal to {converted_amount} {to_curr}")
        else:
            label_result.config(text="Conversion failed. Check currencies.")
    else:
        label_result.config(text="Conversion failed. Please try again later.")

# Load the background image
bg_image = Image.open(r"C:\Users\AMAR9XD\OneDrive\Pictures\Screenshots\Screenshot 2023-11-27 231259.png")  #its the image that i have used , so you need to add the file path that you want to be want as the background
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Input fields, labels, button, and result label
label_amount = tk.Label(root, text="Amount:")
label_amount.pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

label_from_curr = tk.Label(root, text="From Currency:")
label_from_curr.pack()
entry_from_curr = tk.Entry(root)
entry_from_curr.pack()

label_to_curr = tk.Label(root, text="To Currency:")
label_to_curr.pack()
entry_to_curr = tk.Entry(root)
entry_to_curr.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=per_con)
convert_button.pack()

# Result label
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
