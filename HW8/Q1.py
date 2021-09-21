from  datetime import datetime, timedelta
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
    print(type(ali.history[0]['date']))
    aa = ali.history[0]['date']
    bb = datetime.strptime(aa, "%Y/%m/%d, %H:%M")
    print(bb - timedelta(minutes=2) < bb)
    ali.transaction_delta("2021/09/20, 17:35")




