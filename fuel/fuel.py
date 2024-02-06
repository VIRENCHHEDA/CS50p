#creating while loop for reprompting the user for inputting the integer according to the condition
#(try,except)statement for value and zero division error
while True:
    try:
        fuel = input("Fraction: ")
# splitting fuel
        x,y = fuel.split("/")
        x = int(x)
        y = int(y)
# fraction of x and y
        z = x / y
# check if it is less than 1 and stop the loop
        if z <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

# multiply for percentage by 100
p = round(z * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")