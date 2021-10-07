class TextInterface:
    def __init__(self):
        print("Welcome to ticket purchase machine")

    def login(self):
        username = input('user: ')
        password = input('pass: ')
        return username, password

    def show_user_info(self, fullname, type, user_id):
        print(
            f'Dear {fullname}, you have been entered to the ticket purchase system with the id:{user_id} as a/an {type}.')

    def show_events_full_information(self, events):
        event_name = events['event_name']
        event_id = events['event_id']
        date = events['date']
        palce = events['place']
        capacity = events['capacity']
        remaining_capacity = events['remaining_capacity']
        fee = events['fee']
        print(f'{event_id}-{event_name} : {date} in {palce} , price = {fee}$ , solded tickets = {int(capacity) - int(remaining_capacity)}, remaining capacity = {remaining_capacity}')

    def show_events(self, events):
        event_name = events['event_name']
        event_id = events['event_id']
        date = events['date']
        palce = events['place']
        fee = events['fee']

        print(f'{event_id}-{event_name} : {date} in {palce} , price = {fee}$')

    def choose_event_and_quantity(self):
        print("Please Enter the event id and quantity you wanted to buy")
        id = input("id: ")
        count = input("quantity: ")
        return id, count

    def get_discount_code(self):
        return input("Enter your discount code (or press enter): ")

    def show_fee(self, fee, quantity, discount):
        print(
            f'you choosed {quantity} tickets with {fee}$ and {discount*100}% discount ')
        print(f'Total price is: {int(quantity)*float(fee)*(1-discount)}$')

    def ask_payment(self):
        if input('Do you wan to continoue(yes/no): ') == 'yes':
            return True
        return False

    def ask_creat_new_event(self):
        ans = input('Do you want to creat a new event(yes/no)?')
        if ans == 'yes':
            return True
        return False

    def get_event_information(self):
        event_name = input('event name: ')
        date = input('date(month/day/year): ')
        location = input("location: ")
        capacity = input("capacity: ")
        fee = input("fee: ")
        return event_name, date, location, capacity, fee

    def show_information(self, information):
        print(information)
