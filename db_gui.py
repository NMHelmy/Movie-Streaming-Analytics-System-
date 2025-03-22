# Import necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
from datetime import datetime, timedelta

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB server
db = client["MovieStream"]  # Use the "MovieStream" database
movies_collection = db["Movies"]  # Collection for movies
users_collection = db["Users"]  # Collection for users
subscriptions_collection = db["Subscriptions"]  # Collection for subscriptions
views_collection = db["Views"]  # Collection for movie views
admins_collection = db["Admins"]  # Collection for admins

# Global variables to store the current logged-in user's information
current_user_id = None  # Current user's ID
current_username = None  # Current user's name
role = None  # Current user's role (Admin or User)

# Function to generate a unique User ID
def generate_user_id():
    """
    Generates a unique user ID by finding the maximum numeric part of existing user IDs
    and incrementing it by 1.
    """
    users = users_collection.find({}, {"_id": 1})  # Fetch all user IDs
    max_id = 0
    for user in users:
        try:
            numeric_part = int(user["_id"][1:])  # Extract numeric part after 'u'
            if numeric_part > max_id:
                max_id = numeric_part
        except (ValueError, KeyError):
            continue
    new_id = max_id + 1  # Increment the maximum ID
    return f"u{new_id:03d}"  # Format the new ID as 'u001', 'u002', etc.

# Function to handle user login
def login():
    """
    Authenticates the user based on the entered username and user ID.
    Redirects to the main window if login is successful.
    """
    global current_user_id, current_username, role
    username = username_entry.get()  # Get username from the entry field
    user_id = user_id_entry.get()  # Get user ID from the entry field

    # Check if the user ID starts with 'a' (admin) or 'u' (user)
    if user_id.startswith("a"):  # Admin login
        admin = admins_collection.find_one({"_id": user_id, "admin_name": username})
        if admin:
            role = "Admin"
            current_user_id = user_id
            current_username = username
            messagebox.showinfo("Login Success", f"Welcome, {username}!\nRole: {role}")
            login_window.destroy()
            create_main_window(role)  # Open the main window for admin
            return
        else:
            messagebox.showerror("Login Error", "Invalid Admin username or ID.")
            return

    elif user_id.startswith("u"):  # User login
        user = users_collection.find_one({"_id": user_id, "name": username})
        if user:
            role = "User"
            current_user_id = user_id
            current_username = username
            messagebox.showinfo("Login Success", f"Welcome, {username}!\nRole: {role}")
            login_window.destroy()
            create_main_window(role)  # Open the main window for user
            return
        else:
            messagebox.showerror("Login Error", "Invalid User username or ID.")
            return
    else:
        # If the ID doesn't start with 'a' or 'u'
        messagebox.showerror("Login Error", "Invalid ID format. Must start with 'a' for Admin or 'u' for User.")

    # Clear the entry fields after login attempt
    username_entry.delete(0, 'end')
    user_id_entry.delete(0, 'end')

# Function to create the authentication window (Login or Sign-Up)
def create_auth_window():
    """
    Creates the initial authentication window where users can choose to log in or sign up.
    """
    global auth_window
    auth_window = tk.Tk()
    auth_window.title("Login or Sign-Up")
    auth_window.geometry("400x300")
    auth_window.configure(background="white")

    # Configure button styles
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TButton",
        background="blue",
        foreground="white",
        font=("Arial", 14, "bold"),
        padding=5
    )
    style.map(
        "TButton",
        background=[("active", "darkblue")],
        foreground=[("active", "white")]
    )

    # Add a title label
    title_label = ttk.Label(
        auth_window,
        text="Movie Streaming\n        System",
        font=("Helvetica", 28, "bold"),
        foreground="darkblue",
        background="white"
    )
    title_label.pack(pady=20)

    # Buttons for login and sign-up
    def open_login():
        auth_window.destroy()
        create_login_window()

    def open_sign_up():
        auth_window.destroy()
        create_sign_up_window()

    login_button = ttk.Button(auth_window, text="Login", command=open_login, style="TButton")
    login_button.pack(padx=10, pady=20)

    sign_up_button = ttk.Button(auth_window, text="Sign Up", command=open_sign_up, style="TButton")
    sign_up_button.pack(padx=10, pady=20)

    auth_window.mainloop()

# Function to create the login window
def create_login_window():
    """
    Creates the login window where users can enter their username and user ID to log in.
    """
    global username_entry, user_id_entry, login_window

    def clear_placeholder(event, entry, placeholder):
        """Clears the placeholder text when the user clicks on the field."""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(foreground="black")

    def restore_placeholder(event, entry, placeholder):
        """Restores the placeholder text if the field is empty."""
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(foreground="gray")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x400")
    login_window.configure(background="white")

    # Back button to return to the authentication window
    back_button = tk.Button(
        login_window,
        text="← Back",
        font=("Arial", 10, "bold"),
        command=lambda: [login_window.destroy(), create_auth_window()],
        padx=10,
        pady=5
    )
    back_button.place(x=10, y=10)

    # Configure styles
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TButton",
        background="blue",
        foreground="white",
        font=("Arial", 14, "bold"),
        padding=5
    )
    style.map(
        "TButton",
        background=[("active", "darkblue")],
        foreground=[("active", "white")]
    )

    # Title label
    title_label = tk.Label(
        login_window,
        text="Login",
        font=("Helvetica", 22, "bold"),
        fg="black",
        bg="white"
    )
    title_label.pack(pady=20)

    # Username entry field
    username_label = tk.Label(
        login_window,
        text="Username",
        font=("Arial", 12, "bold"),
        fg="black",
        bg="white"
    )
    username_label.pack(pady=(10, 0), padx=20, anchor="w")

    username_frame = tk.Frame(login_window, bg="white")
    username_frame.pack(pady=5, padx=20, fill="x")
    username_icon = tk.Label(username_frame, text="👤", font=("Arial", 16), bg="white", fg="gray")
    username_icon.pack(side="left", padx=5)
    username_entry = ttk.Entry(username_frame, font=("Arial", 12), foreground="gray")
    username_placeholder = "Type your username"
    username_entry.insert(0, username_placeholder)
    username_entry.pack(side="left", fill="x", expand=True, padx=5)
    username_entry.bind("<FocusIn>", lambda e: clear_placeholder(e, username_entry, username_placeholder))
    username_entry.bind("<FocusOut>", lambda e: restore_placeholder(e, username_entry, username_placeholder))

    # Separator
    username_separator = tk.Frame(login_window, height=1, bg="gray")
    username_separator.pack(fill="x", padx=20)

    # User ID entry field
    user_id_label = tk.Label(
        login_window,
        text="User ID",
        font=("Arial", 12, "bold"),
        fg="black",
        bg="white"
    )
    user_id_label.pack(pady=(10, 0), padx=20, anchor="w")

    user_id_frame = tk.Frame(login_window, bg="white")
    user_id_frame.pack(pady=5, padx=20, fill="x")
    user_id_icon = tk.Label(user_id_frame, text="🆔", font=("Arial", 16), bg="white", fg="gray")
    user_id_icon.pack(side="left", padx=5)
    user_id_entry = ttk.Entry(user_id_frame, font=("Arial", 12), foreground="gray")
    user_id_placeholder = "Type your user ID"
    user_id_entry.insert(0, user_id_placeholder)
    user_id_entry.pack(side="left", fill="x", expand=True, padx=5)
    user_id_entry.bind("<FocusIn>", lambda e: clear_placeholder(e, user_id_entry, user_id_placeholder))
    user_id_entry.bind("<FocusOut>", lambda e: restore_placeholder(e, user_id_entry, user_id_placeholder))

    # Separator
    user_id_separator = tk.Frame(login_window, height=1, bg="gray")
    user_id_separator.pack(fill="x", padx=20)

    # Login button
    login_button = ttk.Button(login_window, text="LOGIN", style="TButton", command=login)
    login_button.pack(pady=20, padx=20, ipadx=10, fill="x")

    login_window.mainloop()

# Start the application
create_auth_window()