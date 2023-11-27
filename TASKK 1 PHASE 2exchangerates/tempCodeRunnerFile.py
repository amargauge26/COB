import tkinter as tk
from PIL import Image, ImageTk
import requests

ACCESS_KEY = '12d340f3616665d8083bc22771d31710'
BASE_URL = f'http://api.exchangeratesapi.io/v1/'

root = tk.Tk()
root.title("Currency Converter Hub")

# Function for currency conversion
def per_con():
    amount = float(entry_amount.get())
    from_curr = entry_from_curr.get()
    to_curr = entry_to_curr.get()
    
    params = {'access_key': ACCESS_KEY, 'base': from_curr, 'symbols': to_curr}
    response = requests.get(BASE_URL + 'latest', params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'rates' in data and to_curr in data['rates']:
            conv_amount = amount * data['rates'][to_curr]
            label_result.config(text=f"{amount} {from_curr} is equal to {conv_amount} {to_curr}")
        else:
            label_result.config(text="Conversion failed. Check currencies.")
    else:
        label_result.config(text="Conversion failed. Please try again later.")

# Background image
bg_image = Image.open(r"C:\Users\AMAR9XD\OneDrive\Desktop\curr_exchange.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Display the background image
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
