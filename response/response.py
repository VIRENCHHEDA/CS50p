import validators

email = input("What's your email adress? ")
if validators.email(email) == True:             #check validators documentation in question
    print("Valid")
else:
    print("Invalid")