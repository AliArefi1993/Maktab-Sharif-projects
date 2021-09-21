from datetime import datetime, timedelta


class Account:
    minimum_balance = 10000

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []
        self.transaction_number = 0

    def transaction_delta(self, specified_ate):
        time = datetime.strptime(specified_ate, "%Y/%m/%d, %H:%M")
        for record in self.history:
            his_time = datetime.strptime(record["date"], "%Y/%m/%d, %H:%M")
            if (time + timedelta(minutes=2) > his_time) and (his_time > time - timedelta(minutes=2)):
                print(record)

    def add_rec(self, rec_type, rec_amount):
        self.transaction_number += 1
        date = datetime.now()
        rec = {'item_number': self.transaction_number, 'date': date.strftime("%Y/%m/%d, %H:%M"), 'rec_type': rec_type,
               'rec_amount': rec_amount, 'self.balance': self.balance}
        self.history.append(rec)

    def deposit(self, amount):
        self.balance += amount
        print(f'{self.owner}: deposit succeed')
        self.add_rec("deposit", amount)

    def withdraw(self, amount):
        if self.__check_minimum(amount):
            self.balance += -amount
            print(f'{self.owner}: withdrawal succeed')
            self.add_rec("withdraw", amount)
        else:
            print(f'{self.owner}: withdrawal failed"')

    def transfer(self, another_account, amount):
        if self.__check_minimum(amount):
            self.balance += -amount
            another_account.balance += amount
            self.add_rec(f"transfer to {another_account.owner}", amount)
            another_account.add_rec(f"transfer from {self.owner}", amount)
            print(f'{self.owner}:transfer succeed')
        else:
            print(f'{self.owner}:transfer failed')

    def __check_minimum(self, amount):
        if Account.minimum_balance < self.balance - amount:
            return True
        return False

