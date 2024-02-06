x = input("Input: ")
vowels = ["a","e","i","o","u"]

for char in x:
    if char.lower() in vowels:
        x = x.replace(char,"")
print("Output:",x)

