from bank_account import Account
if __name__ == '__main__':
    ali = Account("ali", 500000)
    mohammad = Account("mohammad", 90000)
    ali.transfer(mohammad, 10000)
    