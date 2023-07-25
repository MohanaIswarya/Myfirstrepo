# pip install tkinter
import tkinter
from tkinter import *
# pip install pyperclip
import pyperclip
import random

root = Tk()
root.geometry("650x320")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)


def generate():  # Function to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)


# function to copy the passcode


def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)


# Labels

fram2 = tkinter.Frame(root)
fram2.pack(padx=5,pady=5)


fram1 = tkinter.Frame(root)
fram1.pack(padx=10,pady=10)

fram3 = tkinter.Frame(root)
fram3.pack(padx=5,pady=5)

fram4 = tkinter.Frame(root)
fram4.pack(padx=10,pady=10)


name=Label(fram2, text="Random Password Generator", font="CopperplateGothicLight 30 bold", anchor="center",justify="center")
name.grid(row=0,column=0)

name1=Label(fram1, text="Enter the number to get password", font="century 9 bold")
name1.grid(row=1,column=0,padx=5,pady=5)


enter=Entry(fram1, textvariable=passlen, font="century 9")
enter.grid(row=1,column=1,padx=5,pady=5)


btn=Button(fram3, text="Tap to get", command=generate, font="century 9 bold", anchor="center",justify="center")
btn.grid(row=2,column=1,padx=10,pady=10)


entry=Entry(fram4, textvariable=passwrd, font="century 9")
entry.grid(row=3,column=0,padx=5,pady=5)


btu1=Button(fram4, text="Tap to copy clipboard", command=copyclipboard, font="century 9 bold")
btu1.grid(row=3,column=1,padx=5,pady=5)



root.mainloop()
