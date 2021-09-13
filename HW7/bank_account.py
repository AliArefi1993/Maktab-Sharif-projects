class Account:
    minimum_balance = 10000

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{self.owner}: deposit succeed')

    def withdraw(self, amount):
        if self.__check_minimum(amount):
            self.balance += -amount
            print(f'{self.owner}: withdrawal succeed')
        else:
            print(f'{self.owner}: withdrawal failed"')

    def transfer(self, another_account, amount):
        if self.__check_minimum(amount):
            self.withdraw(amount)
            another_account.deposit(amount)
            print(f'{self.owner}:transfer succeed')
        else:
            print(f'{self.owner}:transfer failed')

    def __check_minimum(self, amount):
        if Account.minimum_balance < self.balance - amount:
            return True
        return False

