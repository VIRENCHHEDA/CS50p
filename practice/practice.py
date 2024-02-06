##Input Functiom
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

##Checking for valid conditions
def is_valid(s):
    if len(s) < 2 or len(s) > 6:             ##Check for the character length
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:           ##Check for numeric values in 1st and 2nd position
        return False

    for i in range(len(s)):                    ##check for '0' in 1st index
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break

    first_number = [x for x in s if x.isdigit()][0]          ##check if tere is any digit in the middle
    first_number = s.index(first_number)
    number_list = s[first_number:]

    if number_list.isdigit():
        return True
    else:
        return False


    if s.isalnum():
        return True
    else:
        return False
    return


##function call
main()