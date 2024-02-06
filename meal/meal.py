def main():
    time = input("What time is it? ")
    float_time = convert(time)

    if 7.0 <= float_time <= 8.0:
        print("Breakfast time")
    elif 12.0 <= float_time <= 13.0:
        print("Lunch time")
    elif 18.0 <= float_time <= 19.0:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    float_minutes = float(minutes) / 60
    float_hours = float(hours)
    time = float_hours + float_minutes
    return float(time)

if __name__ == "__main__":
    main()
