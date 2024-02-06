x = input("What is answer to the Great Question of Life, the Universe and Everything? " )


if x.strip() == "42" or x.lower().strip() == "forty-two" or x.lower().strip()== "forty two":
    print("yes")
else:
    print("no")