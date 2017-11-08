# Kevin Chen
# 11/08/17
# This Program will build a calculator by Tkinter GUI

import tkinter


root = tkinter.Tk()


root.title("calculator")


def press1():
    """
    This function will make the number one works in this calculator
    :return: nothing
    """
    new_number = number.get()
    new_number = new_number + "1"
    number.set(new_number)


def press2():
    new_number = number.get()
    new_number = new_number + "2"
    number.set(new_number)


def press3():
    new_number = number.get()
    new_number = new_number + "3"
    number.set(new_number)


def press4():
    new_number = number.get()
    new_number = new_number + "4"
    number.set(new_number)


def press5():
    new_number = number.get()
    new_number = new_number + "5"
    number.set(new_number)


def press6():
    new_number = number.get()
    new_number = new_number + "6"
    number.set(new_number)


def press7():
    new_number = number.get()
    new_number = new_number + "7"
    number.set(new_number)


def press8():
    new_number = number.get()
    new_number = new_number + "8"
    number.set(new_number)


def press9():
    new_number = number.get()
    new_number = new_number + "9"
    number.set(new_number)


def press0():
    new_number = number.get()
    new_number = new_number + "0"
    number.set(new_number)


def decimal():
    new_number = number.get()
    new_number = new_number + "."
    number.set(new_number)


def clearall():
    """
    This function will make everything in entryfield become empty
    :return: nothing
    """
    number.set("")


def addition():
    new_number = number.get()
    new_number = new_number + "+"
    number.set(new_number)


def subtraction():
    new_number = number.get()
    new_number = new_number + "-"
    number.set(new_number)


def multiply():
    new_number = number.get()
    new_number = new_number + "*"
    number.set(new_number)


def division():
    new_number = number.get()
    new_number = new_number + "/"
    number.set(new_number)


def delete():
    """
    This function will delete the last number or arithmetic function
    :return: nothing
    """
    new_number = number.get()
    new_number = new_number[:-1]
    number.set(new_number)


def equal():
    """
    This function will calculate everything in entry.
    :return: nothing
    """
    new_number = number.get()
    new_number = str(eval(new_number))
    number.set(new_number)
    

number = tkinter.StringVar()
screen = tkinter.Entry(root, textvariable=number)
screen.grid(column=1, row=1, columnspan=5)
number7 = tkinter.Button(root, text="7", command=press7)
number7.grid(column=1, row=2)

number8 = tkinter.Button(root, text="8", command=press8)
number8.grid(column=2, row=2)

number9 = tkinter.Button(root, text="9", command=press9)
number9.grid(column=3, row=2)

delete = tkinter.Button(root, text="del", command=delete)
delete.grid(column=4, row=2)

clear = tkinter.Button(root, text="AC", command=clearall)
clear.grid(column=5, row=2)

number4 = tkinter.Button(root, text="4", command=press4)
number4.grid(column=1, row=3)

number5 = tkinter.Button(root, text="5", command=press5)
number5.grid(column=2, row=3)

number6 = tkinter.Button(root, text="6", command=press6)
number6.grid(column=3, row=3)

multi = tkinter.Button(root, text="*", width=2, command=multiply)
multi.grid(column=4, row=3)

divide = tkinter.Button(root, text="/", width=2, command=division)
divide.grid(column=5, row=3)

number1 = tkinter.Button(root, text="1", command=press1)
number1.grid(column=1, row=4)

number2 = tkinter.Button(root, text="2", command=press2)
number2.grid(column=2, row=4)

number3 = tkinter.Button(root, text="3", command=press3)
number3.grid(column=3, row=4)

subtract = tkinter.Button(root, text="-", width=2, command=subtraction)
subtract.grid(column=4, row=4)

addition = tkinter.Button(root, text="+", width=2, command=addition)
addition.grid(column=5, row=4)

number0 = tkinter.Button(root, text="0", command=press0)
number0.grid(column=1, row=5, columnspan=2, sticky="EW")

decimal_point = tkinter.Button(root, text=".", command=decimal)
decimal_point.grid(column=3, row=5)

enter = tkinter.Button(root, text="Enter", command=equal)
enter.grid(column=4, row=5, columnspan=2, sticky="EW")

root.mainloop()
