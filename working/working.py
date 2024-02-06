import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    format = re.search("^(([0-9][0-2]?):?([0-5][0-9])?) (AM|PM) to (([0-9][0-2]?):?([0-5][0-9])?) (AM|PM)$", s)
    if format:
        group = format.groups()
        if int(group[1]) > 12 or int(group[5]) > 12:
            raise ValueError
        m = new_format(group[1], group[2], group[3])
        n = new_format(group[5], group[6], group[7])
        return m + " to " + n
    else:
        raise ValueError


def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time




if __name__ == "__main__":
    main()