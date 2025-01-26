import tkinter as tk
from tkinter import messagebox

# Save password to a file
def save_password():
    account = account_entry.get()
    password = password_entry.get()
    if account and password:
        with open("passwords.txt", "a") as file:
            file.write(f"{account}:{password}\n")
        messagebox.showinfo("Success", f"Password saved for account: {account}")
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Retrieve password for a specific account
def retrieve_password():
    account = account_entry.get()
    if account:
        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    stored_account, stored_password = line.strip().split(":")
                    if stored_account == account:
                        password_entry.delete(0, tk.END)
                        password_entry.insert(0, stored_password)
                        messagebox.showinfo("Password Found", f"Password for {account} is: {stored_password}")
                        return
            messagebox.showwarning("Not Found", f"No password found for account: {account}")
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "No passwords stored yet.")
    else:
        messagebox.showwarning("Input Error", "Please enter an account name.")

# GUI Setup
root = tk.Tk()
root.title("Password Manager")

# Account Label and Entry
account_label = tk.Label(root, text="Account:")
account_label.pack(pady=5)

account_entry = tk.Entry(root, width=30)
account_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

# Save and Retrieve Buttons
save_button = tk.Button(root, text="Save Password", width=20, command=save_password)
save_button.pack(pady=10)

retrieve_button = tk.Button(root, text="Retrieve Password", width=20, command=retrieve_password)
retrieve_button.pack(pady=10)

# Run the GUI
root.mainloop()
