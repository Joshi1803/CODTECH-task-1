Name :- Shivam Joshi
Company :- CODTECHITSOLUTION
I'd :-CT4CSEH3956
Domain :- Cyber Security & Ethical Hacking
Duration :- July to August
Mentor :- SANTHOSH KUMAR


Overview
Purpose
The script provides a graphical user interface (GUI) to assess the strength of a password based on various criteria such as length, complexity (use of uppercase, lowercase, digits, special characters), and uniqueness (absence of common passwords and dictionary words). The goal is to help users create stronger passwords.

Key Components
1)Libraries and Dependencies

-re: Regular expressions for pattern matching.
-tkinter (Tkinter): Standard Python library for creating GUIs.
-messagebox from tkinter: For displaying feedback messages.

2)Password Strength Checking Logic

-Length Check: Evaluates if the password length is sufficient.
-Complexity Check: Ensures the password includes uppercase letters, lowercase letters, numbers, and special characters.
-Uniqueness Check: Verifies the password isn't a common password or doesn't contain dictionary words.

3)Tkinter GUI Components

-Main Window: The main application window where all components are placed.
-Label: A text prompt asking the user to enter their password.
-Entry: An input field where the user types the password (masked for security).
-Button: A button that triggers the password strength assessment.
-Messagebox: A popup dialog to display the strength score and feedback.


Script Structure
1)Imports and Data

Imports the required libraries.
Defines lists of common passwords and dictionary words for the uniqueness check.

2)Password Strength Function

check_password_strength(password): This function takes a password as input, evaluates its strength, and returns a score along with feedback.

3)GUI Setup

-on_check_password(): Retrieves the password from the input field, calls the strength check function, and displays the feedback using a message box.
-Tkinter components are created and packed into the main window:
-password_label: Prompts the user to enter their password.
-password_entry: The input field for the password.
-check_button: Triggers the password strength assessment.

4)Main Event Loop![Screenshot 2024-07-22 120342](https://github.com/user-attachments/assets/fd5b4a27-bc01-4867-8f49-4fb0883eb4f5)
![Screenshot 2024-07-22 120342](https://github.com/user-attachments/assets/ca38fcbf-f33f-4bfb-992e-5b8f4f1e5169)


The Tkinter event loop (root.mainloop()) starts, waiting for user interactions.
