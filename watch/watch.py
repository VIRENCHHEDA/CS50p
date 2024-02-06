import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*></iframe>", s):
        pattern = re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)", s)          #(?:) is used in (?:www\.) so that it does not give any return value to the varaible
        if pattern:
            return "https://youtu.be/" + pattern[1]
#you can further shorten the code by using walrus operator for 'if statement'


if __name__ == "__main__":
    main()