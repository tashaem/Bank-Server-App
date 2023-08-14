from bank import Transaction, Bankaccount

def withdraw(username, balance, amount):
    print(balance)
    if amount > balance:
        print("You don't have enough. ")
    else:
        balance -= amount
    print(balance)
    print("withdrawal")

def deposit(username, balance, amount):
    print(balance)
    balance += amount
    print(balance)
    print("withdrawal")

def main():
    index = 0
    while True:
        acc = []
        for i in range(2):
            balance = input("Balance: ")
            username = input("Username: ")
            acc.append(Bankaccount(int(balance), username))

        print(acc[i].username)
        print("--------------------------")
        username = input("Welcome to the Bank! What is your username? ")
        found = False
        count = 0
        while not found:
            for i in range(len(acc)):
                if username == acc[i].username:
                    print("found it")
                    index = i
                    found = True
                else:
                    count+=1
            if count == len(acc):
                username = input("Username not found. Please enter a different username: ")
                found = False
        print(index)

        while True:
            print("""Please choose an action:
            (a) Check balance
            (b) Deposit funds
            (c) Withdraw funds
            (d) Transfer""")
            selection = input()

            if selection not in "abcd":
                print("Your input is invalid. Please choose again.")
                continue
            else:
                if selection == 'c':
                    balance_w = acc[index].balance
                    amount = int(input("Enter the withdrawal amount: "))
                    withdraw(username, balance_w, amount)
                    break


main()