import tkinter as tk
from tkinter import messagebox
from tkinter import font


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")


def update_task():
    try:
        index = listbox.curselection()[0]
        updated_task = entry.get()
        listbox.delete(index)
        listbox.insert(index, updated_task)
        entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")


def main():
    global entry, listbox

    window = tk.Tk()
    window.title("ToDo List")
    window.geometry("500x500")
    window.configure(bg="white")

    label = tk.Label(window, text="  ToDo List", bg="green", fg="black", height=2, width=100,
                     font=("Comic Sans MS", 20, "bold"), anchor="w", justify="left").pack()
    names = tk.Label(window, text="Add Items", bg="white", fg="black", height=1, width=100,
                     font=("calibri", 15, "bold"), anchor="w", justify="left").pack(padx=50, pady=5)

    frame = tk.Frame(window)
    frame.pack()
    frame.configure(bg="white")

    # Create task entry field

    entry = tk.Entry(frame, font=("calibri", 15), highlightbackground="gray", highlightthickness=1)
    entry.pack(padx=20)
    entry.grid(row=0, column=0, ipadx=5, ipady=5, padx=10, pady=10)

    # Create button

    add_button = tk.Button(frame, text="Submit", command=add_task, bg="#006db5", fg="white", width=18)
    add_button.grid(row=0, column=1, ipadx=5, ipady=5, padx=10, pady=10)

    task_name = tk.Label(window, text="Tasks", bg="white", fg="black", height=1, width=40, font=("calibri", 15, "bold"),
                         anchor="w", justify="left").pack(padx=50, pady=5)

    # Create task listbox

    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=10)
    btn_frame.configure(bg="white")

    listbox = tk.Listbox(btn_frame, font=("Helvetica", 12), selectbackground="#a6a6a6", highlightbackground="gray",
                         highlightthickness=1)
    listbox.pack(pady=10)

    listbox.grid(row=2, column=1, ipadx=5, ipady=5, padx=10, pady=10, rowspan=1)

    # Create buttons

    delete_button = tk.Button(btn_frame, text="Delete", command=delete_task, bg="#d31949", fg="white", width=10)
    delete_button.grid(row=2, column=3, ipadx=5, ipady=5, padx=5, pady=5)
    delete_button.configure(relief=tk.RAISED)
    update_button = tk.Button(btn_frame, text="Edit", command=update_task, bg="green", fg="white", width=10)
    update_button.grid(row=2, column=2, ipadx=5, ipady=5, padx=5, pady=5)

    window.mainloop()


if __name__ == '__main__':
    main()
