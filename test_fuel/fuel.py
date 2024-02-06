def main():
    fraction = input("Fraction: ")
    fuel_converted = convert(fraction)
    output = gauge(fuel_converted)
    print(output)



def convert(fraction):
    while True:
        try:
    # splitting fuel
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
    # fraction of x and y
            z = x / y
    # check if it is less than 1 and stop the loop
            if z <= 1:
    # multiply percentage by 100
                p = int(z * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()