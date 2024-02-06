# create a list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date = input("Date: ")
#using try, except statement here
    try:
        month,day,year = date.split("/")
        month = month.replace(" ","")
        year = year.replace(" ","")
        if  (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
             break
    except:
        try:
# replacing the vaiable names of month, day here
            m,d,year = date.split(" ")

            for i in range(len(months)):
                if m == months[i]:
                    month = i+1
            if "," in date:
                day = d.replace(",","")
            if  (1 <= int(month) <= 12) and  (1 <= int(day) <= 31):
                    break
        except:
            print()
            pass
# print(f"{n:02}") this syntax in used here for changing to double digits months and days
print(f"{year}-{int(month):02}-{int(day):02}",sep="")