import unittest
from ticket import Ticket, Event, Db, User, Discount
from textTicket import TextInterface


class TestEventMethods(unittest.TestCase):

    def setUp(self):
        self.db = Db()
        self.re_client = self.db.redis_client

    def test_save(self):
        self.event = Event(self.db, 'concert_test',
                           '10/10/2021', 'Kerman', 200, 200, 10)
        self.event.save()
        self.assertIsNotNone(self.re_client.hmget(
            f'event:{self.event.event_id}:info', 'date'))

    def test_get_all_events(self):
        self.event = Event(self.db, 'concert_test',
                           '10/10/2021', 'Kerman', 200, 200, 10)
        self.event.save()
        self.assertIsNotNone(Event.get_all_events(self.db))

    def test_get_event_info(self):
        self.event = Event(self.db, 'concert_test',
                           '10/10/2021', 'Kerman', 200, 200, 10)
        self.event.save()
        self.assertIsNotNone(Event.get_event_info(
            self.db, 'event:{self.event.event_id}:info'))

    def test_update_event(self):
        self.event = Event(self.db, 'concert_test',
                           '10/10/2021', 'Kerman', 200, 200, 10)
        self.event.save()
        print()
        self.assertEqual(self.re_client.hmget(
            f'event:{self.event.event_id}:info', 'date')[0], '10/10/2021')


class TestDiscountMethods(unittest.TestCase):

    def setUp(self):
        self.db = Db()
        self.re_client = self.db.redis_client

    def test_save(self):
        self.discount = Discount(self.db, 'abc', .3, 'student')
        self.discount.save()
        self.assertIsNotNone(self.re_client.hmget(
            f'discount:{self.discount.discount_code}', 'discount'))


class TestUserMethods(unittest.TestCase):

    def setUp(self):
        self.db = Db()
        self.re_client = self.db.redis_client

    def test_save(self):
        self.user = User(self.db, 'mhm', 'Mohammad', '234', 'employee')
        self.user.save()
        self.assertIsNotNone(self.re_client.hmget(
            f'user:{self.user.user_id}:info', 'discount'))

    def test_get_all_users(self):
        self.event = User(self.db, 'mhm', 'Mohammad', '234', 'employee')
        self.event.save()
        self.assertIsNotNone(User.get_all_users(self.db))

    def test_get_user_info(self):
        self.user = User(self.db, 'mhm', 'Mohammad', '234', 'employee')
        self.user.save()
        self.assertIsNotNone(User.get_user_info(
            self.db, 'user:{self.user.user_id}:info'))

    def test_find_user(self):
        self.user = User(self.db, 'mhm', 'Mohammad', '234', 'employee')
        self.user.save()
        self.assertIsNotNone(self.user.find_user(self.db, 'mhm', '234'))
        self.assertIsNone(self.user.find_user(self.db, 'mhm', '23466666'))


class TestDbMethods(unittest.TestCase):

    def setUp(self):
        self.db = Db()

    def test_save(self):
        self.re_client = self.db.redis_client
        self.assertIsNotNone(self.re_client)


class TestTicketMethods(unittest.TestCase):

    def setUp(self):
        self.db = Db()
        self.re_client = self.db.redis_client

    def test_valid_discount_code(self):

        self.ticket = Ticket(TextInterface())
        self.discount = Discount(self.db, 'abc', .3, 'student')
        self.discount.save()
        valid_discount, discount, discount_user_type = self.ticket.valid_discount_code(
            'abc')
        self.assertEqual(valid_discount, True)
        self.assertEqual(discount, 0.3)
        self.assertEqual(discount_user_type, 'student')


if __name__ == "__main__":
    unittest.main(verbosity=2)
