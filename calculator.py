from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("380x380")
window.resizable(0, 0)


# btn clear function
def clear_btn():
    global exp
    exp = ""
    input_text.set("")


# click button function
def click_btn(i):
    global exp
    exp = exp + str(i)
    input_text.set(exp)


# equalto (ans for input) function
def equal_btn():
    global exp
    result = str(eval(exp))
    input_text.set(result)
    exp = ""


exp = ""

# to get instance of an input
input_text = StringVar()

# creating frame for entry
input_frame = Frame(window, width=300, height=50, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)

user_input = Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), width="50", bg="black", fg="white",
                   bd=0, justify=RIGHT, )
user_input.grid(row=0, column=0)
user_input.pack(ipady=10)

# creating another frame for buttons
btns_frame = Frame(window, width=312, height=272.5, bg="black")
btns_frame.pack()

clear = Button(btns_frame, text="c", font=("bold"), fg="red", width=32, height=3, bd=0, bg="#2c041c", cursor="hand2",
               command=lambda: clear_btn()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", font=("bold"), fg="#b65fcf", width=10, height=3, bd=0, bg="#2c041c",
                cursor="hand2", command=lambda: click_btn("/")).grid(row=0, column=3, padx=1, pady=1)

seven = Button(btns_frame, text="7", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c",
               cursor="hand2", command=lambda: click_btn(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c",
               cursor="hand2", command=lambda: click_btn(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c", cursor="hand2",
              command=lambda: click_btn(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", font=("bold"), fg="#b65fcf", width=10, height=3, bd=0, bg="#2c041c",
                  cursor="hand2", command=lambda: click_btn("*")).grid(row=1, column=3, padx=1, pady=1)

four = Button(btns_frame, text="4", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c", cursor="hand2",
              command=lambda: click_btn(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c", cursor="hand2",
              command=lambda: click_btn(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c", cursor="hand2",
             command=lambda: click_btn(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", font=("bold"), fg="#b65fcf", width=10, height=3, bd=0, bg="#2c041c",
               cursor="hand2", command=lambda: click_btn("-")).grid(row=2, column=3, padx=1, pady=1)

one1 = Button(btns_frame, text="1", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c", cursor="hand2",
              command=lambda: click_btn(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c", cursor="hand2",
             command=lambda: click_btn(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", font=("bold"), fg="#0077b6", width=10, height=3, bd=0, bg="#2c041c",
               cursor="hand2", command=lambda: click_btn(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", font=("bold"), fg="#b65fcf", width=10, height=3, bd=0, bg="#2c041c", cursor="hand2",
              command=lambda: click_btn("+")).grid(row=3, column=3, padx=1, pady=1)

zero1 = Button(btns_frame, text="0", font=("bold"), fg="#0077b6", width=21, height=3, bd=0, bg="#2c041c",
               cursor="hand2", command=lambda: click_btn(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", font=("bold"), fg="#b65fcf", width=10, height=3, bd=0, bg="#2c041c",
               cursor="hand2", command=lambda: click_btn(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", font=("bold"), fg="white", width=10, height=3, bd=0, bg="#b65fcf", cursor="hand2",
                command=lambda: equal_btn()).grid(row=4, column=3, padx=1, pady=1)

window.mainloop()
