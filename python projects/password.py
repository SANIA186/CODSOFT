import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(self.root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(self.root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, columnspan=2, padx=10, pady=10)

        self.password_label = tk.Label(self.root, text="")
        self.password_label.grid(row=2, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        password_length = int(self.length_entry.get())
        if password_length <= 0:
            self.password_label.config(text="Invalid length!")
            return

        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
        self.password_label.config(text=generated_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
