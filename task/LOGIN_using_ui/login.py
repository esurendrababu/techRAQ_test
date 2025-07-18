import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="login_db"
)
cursor = conn.cursor()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both fields")
        return

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        login_frame.pack_forget()
        logout_frame.pack()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def logout():
    logout_frame.pack_forget()
    login_frame.pack()
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

#Ui
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

# Login 
login_frame = tk.Frame(root)
tk.Label(login_frame, text="Username").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password").pack()
password_entry = tk.Entry(login_frame, show='*')
password_entry.pack()

tk.Button(login_frame, text="Login", command=login).pack(pady=10)
login_frame.pack()

# Logout 
logout_frame = tk.Frame(root)
tk.Label(logout_frame, text="You are logged in!").pack(pady=10)
tk.Button(logout_frame, text="Logout", command=logout).pack()

root.mainloop()
