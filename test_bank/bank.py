def main():
    greeting = input("Greetings ")
    value_print = value(greeting)
    print(value_print)


def value(greeting):
    greeting = greeting.strip().lower()
    if "hello" in greeting:
        return 0

    elif "h" == greeting[0]:
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()