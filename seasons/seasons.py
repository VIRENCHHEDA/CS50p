from datetime import date
import re
import sys
import inflect
p = inflect.engine()



def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalid date")
    my_date = date(int(year),int(month),int(day))
    date_today = date.today()             #date.today() is used for getting current day's date(given in hint)
    diff = date_today - my_date
    total = diff.days * 24 * 60
    output = p.number_to_words(total, andword="")     #p.number_to_words is used to convert nos to words and (andword="") is used to remove 'and' in string
    print(output.capitalize() + " minutes")           #capitalize() is used to capitalize first letter



def check_birthday(birth_date):
        if re.search(r"^(\d{4})-(\d{2})-(\d{2})$",birth_date):
            year,month,day = birth_date.split("-")
            return year, month, day



if __name__ == "__main__":
    main()