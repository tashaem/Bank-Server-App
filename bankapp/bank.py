# BankAccount class
import datetime

class Transaction:
    def __init__(self, transaction_id, crdr, amount_t):
        self.transaction_id = transaction_id
        self.date = datetime.now()
        self.crdr = crdr
        self.amount = amount_t

class Bankaccount:
    def __init__(self, balance, username):
        self.balance = balance
        self.username = username
        self.__transaction_list = []

    def add_transaction(self, Transaction):
        self.__transaction_list.append(Transaction)



