import random


def main():
    level = get_level()
    score = simulate_game(level)
    print("score: ", score)


def get_level():                                            #getting input of "value" which should be 1,2,3
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
                pass
    return level


def generate_integer(level):                                #generating random integer
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y



def question(x,y):           #the math problem
    tries = 1
    while tries <= 3:
        try:
            answer= int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True                       #return value and exit loop if answer == correct
            else:
                tries += 1                        #if ans is != correct
                print("EEE")
        except:                                   #if ans != integer
            tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


def simulate_game(level):                #to have 10 questions
    count_round = 1
    score = 0
    while count_round <= 10:
        x,y = generate_integer(level)
        response = question(x,y)
        if response == True:
            score += 1
        count_round += 1
    return score                         #to have final score in the end








if __name__ == "__main__":
    main()