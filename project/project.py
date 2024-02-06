#imports
import pandas as pd

#initial cleaning
df=pd.read_csv(r'/workspaces/144625018/project/atm.csv')
df.drop(['Unnamed: 0'] ,axis=1, inplace=True)


def main():
    user_account = auth_ac()
    if user_account:
        home(*user_account)

#to check the Account Number
def auth_ac():
    print('-------------Enter your account number--------------')
    user_ac = str(input())
    if (df['Account Number'] == user_ac).any():
        pin(user_ac)
    else:
        print("_______WRONG AC NUMBER________")
        print("-----Enter valid ac number----")

#to check the pin for given Account Number
def pin(user_ac):
    user_ac = user_ac
    count = 3
    while count > 0:
        try:
            print("\n\t_____{} attempts left!_____".format(count))
            print('-------------Enter the 4 digit pin---------------')
            entered_pin = int(input())
            if (df['Pin'] == entered_pin).any():
                name = df.loc[df['Account Number'] == user_ac, 'Name'].iloc[0]
                balance = df.loc[df['Account Number'] == user_ac, 'Balance'].iloc[0]
                home(user_ac, entered_pin, name, balance)
                break
            else:
                count -= 1
                print("\t_______WRONG PIN!!________")
                print("\n\t_____{} attempts left!_____".format(count))
        except (ValueError):
            pass

# homepage navigation
def home(user_ac, entered_pin, name, balance):
    name=name
    balance=balance
    user_ac=user_ac
    entered_pin=entered_pin
    while True:
        print("\t_____WELCOME!_____")
        print("\t____{}____".format(name))
        print("\n1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            display_balance(balance)
        elif choice == "2":
            amount = float(input("\nEnter the deposit amount: $"))
            balance = deposit(balance, amount)
        elif choice == "3":
            amount = float(input("\nEnter the withdrawal amount: $"))
            balance = withdraw(balance, amount)
        elif choice == "4":
            new_pin = int(input("\nEnter new PIN: "))
            entered_pin = change_pin(user_ac,entered_pin, new_pin)
        elif choice == "5":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")



def display_balance(balance):
    print(f"\nAccount Balance: Rs.{balance:.2f}\n")

def deposit(balance, amount):
    balance += amount
    print(f"\n-----DEPOSIT SUCCESFULL!-----.{amount:.2f}")
    print(f"\nDeposited: Rs.{amount:.2f}")
    display_balance(balance)
    return balance

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        print(f"\n-----WITHDRAWAL SUCCESFULL!-----.{amount:.2f}")
        print(f"\nWithdrawn: Rs.{amount:.2f}")
        display_balance(balance)
        return balance
    else:
        print("\nInsufficient funds.")
        return balance

def change_pin(user_ac,pin, new_pin):
    print("\n-----PIN CHANGED SUCCESSFULLY.-----")
    df.replace(df.loc[df['Account Number'] == user_ac, 'Pin'].iloc[0],new_pin, inplace=True)
    return new_pin




if __name__ == "__main__":
    main()



df.to_csv("atm.csv")