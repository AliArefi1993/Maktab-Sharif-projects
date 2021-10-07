from datetime import datetime, timedelta
from bank_account import Account
if __name__ == '__main__':
    ali = Account("ali", 500000)
    mohammad = Account("mohammad", 90000)
    ali.transfer(mohammad, 2000)
    ali.deposit(10000)
    ali.deposit(10000)
    ali.deposit(10000)
    print(ali.history)
    print(mohammad.history)
    ali.transaction_delta("2021/09/28, 20:20")
