import random


while True:
    try:
        n = int(input("Level:"))                           #taking input for level
        random_num = random.randint(1,n)                   # using 'randint' for getting a random no
        if int(n) > 0:                                     # the level no should be +ve no
            user_guess = int(input("Guess:"))              # taking user input as guess for the no
            if user_guess < random_num:                    # using conditions for printing statement in output
                print("Too small!")
            elif user_guess > random_num:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass
