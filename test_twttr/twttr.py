def main():
    x = input("Input: ")
    print("Output: " + shorten(x))

def shorten(word):
    for vowel in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        word = word.replace(vowel, "").strip()
    return word


if __name__ == "__main__":
    main()
