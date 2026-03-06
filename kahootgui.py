import random
import string
import tkinter as tk
import logging
import zipfile
import platform  # Added for OS info
import os
from datetime import datetime

# Updated filename to be OS-friendly (dashes instead of colons)
log_filename = datetime.now().strftime("%I-%M-%S_%B-%d-%Y.log")
zip_filename = log_filename.replace(".log", ".zip")

# 1. Setup Logging
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - OS: %(os_info)s - CODE: %(message)s',
    datefmt='%I:%M:%S %p'
)

# Inject OS info into logs
old_factory = logging.getLogRecordFactory()
def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.os_info = f"{platform.system()} {platform.release()}"
    return record
logging.setLogRecordFactory(record_factory)

def zip_log():
    """Compresses the current log file into a zip."""
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as archive:
            archive.write(log_filename)
    except Exception as e:
        print(f"Zip failed: {e}")

def generate_code():
    rc_list = [random.choice(string.ascii_uppercase + string.digits) for _ in range(6)]
    new_code = "".join(rc_list)
    timestamp = datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")

    status_label.config(text=f"Last generated at: {timestamp}")
    result_label.config(text="Room Code: " + new_code)

    logging.info(new_code)
    zip_log()
    print(f"Logged & Zipped: {new_code} on {platform.system()}")

root = tk.Tk()
root.title("Kahoot Number Generator")
root.geometry("500x400")

result_label = tk.Label(root, text="Click to generate", font=("Arial", 20))
result_label.pack(pady=40)

btn = tk.Button(root, text="Generate Code", command=generate_code, font=("Arial", 14))
btn.pack(pady=20)

status_label = tk.Label(root, text="Not yet generated", fg="gray")
status_label.pack(pady=10)

os_Label = tk.Label(root, text=f"Operating System: {platform.system()}", fg="blue")

credit_label = tk.Label(root, text="Created and developed by @KeresDev and @TheMadPerson\nLicensed under GNU GPL-2.0\nThis software is free and Open Source DO NOT SELL",
                        font=("Arial", 8, "italic"), wraplength=350, justify="center", fg="gray")
credit_label.pack(side="bottom", pady=10)
os_Label.pack(side="bottom", pady=10)
root.mainloop()
