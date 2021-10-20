from os import name
import redis
import datetime


class Log:
    def add_log(description):
        with open('HW10/log.txt', 'a') as f:
            print(datetime.datetime.now(), description, file=f)


class Ticket:
    def __init__(self, interface):
        self.db = Db()
        self.interface = interface
        self.redis_client = self.db.redis_client
        if not User.get_all_users(self.db):
            admin = User(self.db, 'admin', 'Ali', '12345', 'admin')
            admin.save()
            student = User(self.db, 'student', 'Reza', '1', 'student')
            student.save()
            employee = User(self.db, 'employee', 'Mohammad', '2', 'employee')
            employee.save()
            user = User(self.db, 'user', 'Hadi', '3', 'user')
            user.save()

    def start(self):
        while True:
            self.run()

    def run(self):
        username, password = self.interface.login()
        logged_in_user = User.find_user(self.db, username, password)
        if (logged_in_user):
            Log.add_log(
                f"{username} has been logged in as {logged_in_user['type']} successfully")
            self.interface.show_user_info(
                logged_in_user['fullname'], logged_in_user['type'], logged_in_user['user_id'])
            if logged_in_user['type'] == 'admin':
                self.run_admin()
            else:
                for event in Event.get_all_events(self.db):
                    self.interface.show_events(
                        Event.get_event_info(self.db, event))
            event_id, quantity = self.interface.choose_event_and_quantity()
            choosed_event = Event.get_event_info(
                self.db, f"event:{event_id}:info")
            discount_code = self.interface.get_discount_code()
            self.valid_discount_code(discount_code)
            valid_discount, discount, discount_user_type = self.valid_discount_code(
                discount_code)
            if valid_discount and discount_user_type == logged_in_user['type']:
                self.interface.show_information(
                    f"Your discount code is valid and your is : {discount*100}%")

            else:
                discount = 0
                self.interface.show_information(
                    f"Your discount code isn't valid.")
                Log.add_log(
                    f"Entered discount code isn't valid for {choosed_event['event_name']}")
            self.interface.show_fee(choosed_event['fee'], quantity, discount)
            if int(choosed_event['remaining_capacity']) >= int(quantity):
                if self.interface.ask_payment():
                    self.interface.show_information(
                        f'You successfuly bought {quantity} tickets.')
                    Event.update_event(self.db, choosed_event, quantity)
                    Log.add_log(
                        f"{quantity} tickets from {choosed_event['event_name']} has been sold")
            else:
                self.interface.show_information(
                    "sorry there isn't enough free seat for you.")
                Log.add_log(
                    f"There isn't {quantity} free seat from {choosed_event['event_name']}. ")

    def run_admin(self):
        if self.interface.ask_creat_new_event():
            event_name, date, location, capacity, fee = self.interface.get_event_information()
            new_event = Event(self.db, event_name, date,
                              location, capacity, capacity, fee)
            new_event.save()
        for event in Event.get_all_events(self.db):
            self.interface.show_events_full_information(
                Event.get_event_info(self.db, event))

    def valid_discount_code(self, discount_code):
        active_discount = self.redis_client.hmget(
            f"discount:{discount_code}", 'discount', 'user_type')
        if active_discount != [None, None]:
            discount = active_discount[0]
            discount_user_type = active_discount[1]
            return True, float(discount), discount_user_type
        return False, 0, None


class User:
    def __init__(self, db, username, fname, password, type):
        self.username = username
        self.fname = fname
        self.password = password
        self.type = type
        self.re_client = db.redis_client
        self.user_id = self.re_client.get("user_id")
        self.re_client.incr("user_id")

    def save(self):
        self.re_client.hset(
            name=f"user:{self.user_id}:info", mapping={
                "user_id": self.user_id, "username": self.username, "fullname": self.fname,
                "password": self.password, "type": self.type}
        )

    @ staticmethod
    def get_user_info(db, key):
        return db.redis_client.hgetall(key)

    @ staticmethod
    def get_all_users(db):
        return db.redis_client.keys(pattern="user:*:info")

    @ staticmethod
    def find_user(db, username, password):
        all_users = User.get_all_users(db)
        for user in all_users:
            current_user = User.get_user_info(db, user)
            if current_user['username'] == username and current_user['password'] == password:
                return current_user


class Db:
    def __init__(self):
        self.redis_client = redis.Redis(db=2, decode_responses=True)
        self.redis_client.setnx("event_id", 1)
        self.redis_client.setnx("user_id", 1)


class Event:
    def __init__(self, db, event_name, event_date, place, capacity, remaining_capacity, fee):
        self.event_name = event_name
        self.event_date = event_date
        self.place = place
        self.capacity = capacity
        self.remaining_capacity = remaining_capacity
        self.fee = fee
        self.re_client = db.redis_client
        self.event_id = self.re_client.get("event_id")
        self.re_client.incr("event_id")

    def save(self):
        self.re_client.hset(
            name=f"event:{self.event_id}:info", mapping={"event_name": self.event_name, "event_id": self.event_id,
                                                         "date": self.event_date, "place": self.place, "capacity": self.capacity,
                                                         "remaining_capacity": self.remaining_capacity, "fee": self.fee}
        )

        Log.add_log(f"new event({self.event_name}) has been created")

    @ staticmethod
    def get_all_events(db):
        return db.redis_client.keys(pattern="event:*:info")

    @ staticmethod
    def get_event_info(db, key):
        return db.redis_client.hgetall(key)

    @staticmethod
    def update_event(db, choosed_event, quantity):
        remaining_capacity = int(
            choosed_event['remaining_capacity']) - int(quantity)
        db.redis_client.hset(name=f"event:{choosed_event['event_id']}:info", mapping={
                             "remaining_capacity": remaining_capacity})


class Discount:
    def __init__(self, db, discount_code, discount, user_type):
        self.discount_code = discount_code
        self.discount = discount
        self.re_client = db.redis_client
        self.user_type = user_type

    def save(self):
        self.re_client.hset(name=f"discount:{self.discount_code}",  mapping={"discount_code": self.discount_code,
                            "discount": self.discount, "user_type": self.user_type})

    # @ staticmethod
    # def get_all_discounts(db):
    #     return db.redis_client.keys(pattern="discount:*")

    # @ staticmethod
    # def get_discount_info(db, key):
    #     return db.redis_client.hgetall(key)
