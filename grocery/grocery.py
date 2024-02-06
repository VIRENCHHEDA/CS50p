#creating empty dict
grocery = {}

while True:
    try:
        list = input().lower()

        if list in grocery:
# adding key value by 1 if input is more than once
            grocery[list] += 1
        else:
# key value will remain 1 if input for key is only once
            grocery[list] = 1

    except EOFError:
# sorted func is used to arrange alphabetically in dict
# keys() returns a list of the keys
        for key in sorted(grocery.keys()):
# here upper() is used for all letters in key to be of uppercase
            print (grocery[key], key.upper())
        break
