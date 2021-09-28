import datetime


class AmountError(Exception):
    pass


class ValidationError(Exception):
    pass


class Card:
    id = 1000

    def __init__(self):
        self.valid = True
        self.id_genrator()

    @classmethod
    def id_genrator(cls):
        cls.id += 1


class SingleWayCard(Card):
    def __init__(self):
        super().__init__()

    def use_card(self):
        if self.valid:
            self.valid = False
            return True
        raise ValidationError


class CreditCard(Card):
    def __init__(self, credit):
        super().__init__()
        self.credit = credit

    def use_card(self, amount):
        if self.credit > amount:
            self.credit = self.credit - amount
            return True
        raise AmountError

    def charge(self, amount):
        self.credit = self.credit + amount


class TimeCreditCard(CreditCard):
    def __init__(self, credit, valid_date):
        super().__init__(credit)
        self.valid_date = valid_date

    def use_card(self, amount):
        if datetime.datetime.now() < self.valid_date:
            return super().use_card(amount)
        raise ValidationError

    def charge(self, amount, new_expire_date):
        super().charge(amount)
        self.valid_date = new_expire_date


# b = TimeCreditCard(500000, datetime.datetime(2023, 3, 3))
# print(b.use_card(1000))
# b.charge(99000, datetime.datetime(2027, 3, 2))
# try:
#     print(b.use_card(1099900009999))
# except AmountError:
#     print("AmountError")
# print(b.valid_date, b.credit)
# print(b.use_card((9999)))
# print(b.id)
