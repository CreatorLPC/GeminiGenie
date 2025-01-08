# AIzaSyD8Kz_b-9MJoYW755ckVgxs-LW_nx9fZ6E api key
import module as gemini

import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.title("GeminiGenie")
root.geometry("800x300")  # Set the window size (800x300)

# Label
label = tk.Label(root, text="What file would you like me to rewrite?", font=("Arial", 14))
label.pack(pady=20)

# Function to handle "Choose a file" button click
def choose_file():
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        print(f"Chosen file: {file_path}")
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            content = file.read()
            print(content)
            # print(f"Content of the file: {content}")

        # Here, you can add the logic to work with the chosen file

# Function to handle "Share" button click
def share():
    print("Sharing...")
    # Add sharing logic here

# Function to handle "Upload to Firebase" button click
def upload_to_firebase():
    print("Uploading to Firebase...")
    # Add logic to upload the file to Firebase here

# Buttons
choose_file_button = tk.Button(root, text="Choose a file", width=20, command=choose_file)
choose_file_button.pack(pady=10)

share_button = tk.Button(root, text="Share", width=20, command=share)
share_button.pack(pady=10)

upload_button = tk.Button(root, text="Upload to Firebase", width=20, command=upload_to_firebase)
upload_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
