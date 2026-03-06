import random
import string
import tkinter as tk
from datetime import datetime # Fix 1: Specific import

def generate_code():
    # Generate the random 6-character code
    rc_list = [random.choice(string.ascii_uppercase + string.digits) for _ in range(6)]
    new_code = "".join(rc_list)

    # Fix 2: Indentation and calling the datetime class correctly
    timestamp = datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")

    # Update labels
    status_label.config(text=f"Last generated at: {timestamp}")
    result_label.config(text="Room Code: " + new_code)
    print("Generated: " + new_code)

root = tk.Tk()
root.title("Kahoot Number Generator")
root.geometry("400x300")

# UI Elements
result_label = tk.Label(root, text="Click to generate", font=("Arial", 20))
result_label.pack(pady=40)

btn = tk.Button(root, text="Generate Code", command=generate_code, font=("Arial", 14))
btn.pack(pady=20)

status_label = tk.Label(root, text="Not yet generated", fg="gray")
status_label.pack(pady=10)

root.mainloop()
