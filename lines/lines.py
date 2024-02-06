import sys

def main():
    # Check the command-line arguments
    arg_check()

    # Print the number of lines of code
    print(get_lines(sys.argv[1]))


def arg_check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def get_lines(filename):
    line_count = 0
    try:
        with open(filename) as file:
            for line in file:
                if not line.lstrip().startswith("#") and not line.isspace():    #for not counting comments(lines starting with '#') and not counting blank lines or empty space lines
                    line_count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return line_count


if __name__== "__main__":
    main()