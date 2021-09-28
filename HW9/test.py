import unittest

from cards import Card, SingleWayCard, ValidationError, CreditCard, TimeCreditCard, datetime, AmountError


class TestCardMethods(unittest.TestCase):

    def setUp(self):
        self.card = Card()

    # Test id of each card
    def test_id_genrator(self):
        self.assertEqual(self.card.id, 1001)
        self.card = Card()
        self.assertEqual(self.card.id, 1002)


class TestSingleWayCardMethods(unittest.TestCase):

    def setUp(self):
        self.singleWayCard = SingleWayCard()

    # Test use of single way card
    def test_use_card(self):
        self.assertEqual(self.singleWayCard.use_card(), True)
        with self.assertRaises(ValidationError):
            self.singleWayCard.use_card()


class TestCreditCardMethods(unittest.TestCase):

    def setUp(self):
        self.creditCard = CreditCard(10000)

    # Test use of credit card
    def test_use_card(self):
        self.assertEqual(self.creditCard.use_card(2000), True)
        self.assertEqual(self.creditCard.credit, 8000)
        with self.assertRaises(AmountError):
            self.creditCard.use_card(900000)

    # test charging of credit card
    def test_charge(self):
        self.assertEqual(self.creditCard.credit, 10000)
        self.creditCard.charge(5000)
        self.assertEqual(self.creditCard.credit, 15000)


class TestTimeCreditCardMethods(unittest.TestCase):

    def setUp(self):
        self.timeCreditCard = TimeCreditCard(
            10000, datetime.datetime(2023, 3, 3))

    # Test use of time credit card
    def test_use_card(self):
        self.assertEqual(self.timeCreditCard.use_card(2000), True)
        with self.assertRaises(AmountError):
            self.timeCreditCard.use_card(200033333)
        self.assertEqual(self.timeCreditCard.credit, 8000)
        self.timeCreditCard.charge(0, datetime.datetime(2000, 3, 3))
        with self.assertRaises(ValidationError):
            self.timeCreditCard.use_card(2000)

    # Test charging of time credit card
    def test_charge(self):
        self.assertEqual(self.timeCreditCard.credit, 10000)
        self.assertEqual(self.timeCreditCard.valid_date,
                         datetime.datetime(2023, 3, 3))
        self.timeCreditCard.charge(5000, datetime.datetime(2025, 3, 3))
        self.assertEqual(self.timeCreditCard.credit, 15000)
        self.assertEqual(self.timeCreditCard.valid_date,
                         datetime.datetime(2025, 3, 3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
