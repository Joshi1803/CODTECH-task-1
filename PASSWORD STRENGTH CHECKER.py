import re
import tkinter as tk
from tkinter import messagebox

# Sample dictionary and common password lists
common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty"]
dictionary_words = ["password", "admin", "login", "welcome", "monkey", "letmein", "abc123"]

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) < 8:
        feedback.append("Password is too short. Minimum length is 8 characters.")
    elif len(password) < 12:
        score += 1
        feedback.append("Password length is acceptable, but longer passwords are stronger.")
    else:
        score += 2
        feedback.append("Password length is strong.")

    # Complexity Check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    if re.search(r'\W', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Uniqueness Check
    if password in common_passwords:
        feedback.append("Password is too common.")
    elif any(word in password.lower() for word in dictionary_words):
        feedback.append("Password contains dictionary words, which makes it weaker.")
    else:
        score += 2
        feedback.append("Password does not contain common dictionary words.")

    # Final Feedback
    if score >= 6:
        feedback.append("Your password is strong.")
    elif score >= 4:
        feedback.append("Your password is moderate. Consider improving it.")
    else:
        feedback.append("Your password is weak. Consider changing it.")

    return score, feedback

def on_check_password():
    password = password_entry.get()
    score, feedback = check_password_strength(password)
    feedback_message = f"Password Strength Score: {score}\n" + "\n".join(feedback)
    messagebox.showinfo("Password Strength Feedback", feedback_message)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the components in the window
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show='~')
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=on_check_password)
check_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
