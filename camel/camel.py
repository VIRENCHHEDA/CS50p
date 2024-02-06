x = input("camelCase: ")

for char in x:
    if char.isupper():
        print("_"+ char.lower(),end="")
    else:
        print(char,end="")
print()



