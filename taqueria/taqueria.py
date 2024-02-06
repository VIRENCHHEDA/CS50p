#dictionary
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# set amount == 0
amount = 0
# used while loop
while True:
# used try, except statement for EOFEerror ()
    try:
# input is with title function for 1st letter capital
        order = input("Item: ").title()
        if order in menu:
# amount is added with keyvalue which will keep on adding with new input in loop
            amount = amount + menu[order]
# here ' "{:.2f}".format(amount)' is used for 2 decimal no.s (syntax)
            print("total: ","$", "{:.2f}".format(amount) , sep="")
    except EOFError:
# printing new line for clean terminal window
        print()
        break