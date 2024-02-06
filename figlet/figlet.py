import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()


#You can then get a list of available fonts with code like this: figlet.getFonts()
#You can set the font with code like this, wherein f is the font’s name as a str: figlet.setFont(font=f)
#you can output text in that font with code like this, wherein s is that text as a str: print(figlet.renderText(s))


# No command-line argument (just the script name)
if len(sys.argv) == 1:
    figlet.setFont(font=choice(figlet.getFonts()))
    print("Output:", figlet.renderText(input("Input:  ")), sep="\n")
    # Gets the input first, converts it and prints the output
    # \n separates arguments in different lines

# Two command-line arguments
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
    print("Output:", figlet.renderText(input("Input:  ")), sep="\n")

else:
    sys.exit("Invalid usage")



