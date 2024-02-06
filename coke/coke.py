amount_due = int(50)

while amount_due > 0:
    print("Amount Due:",amount_due)
    x = int(input("Insert Coin: "))
    if x == 25 or x == 10 or x == 5:
        amount_due = (amount_due-x)
        if amount_due <= 0:
            print("Change Owed:",amount_due*-1 )

