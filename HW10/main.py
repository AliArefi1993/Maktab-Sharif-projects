from ticket import Event, Db, User, Ticket, Discount
import datetime

db = Db()

# dis = Discount(db, 'discod', 0.25)
# dis.save()
# print(db.redis_client.get("discount:discod"), 99877)
# print(Discount.get_discount_info(db, Discount.get_all_discounts(db)[0]))

dis = Discount(db, '2', 0.40, 'admin')
dis.save()
dis = Discount(db, '1', 0.10, 'user')
dis.save()
# print(Discount.get_all_discounts(db))
# print(Discount.get_discount_info(db, Discount.get_all_discounts(db)[0]))

# print(User.get_all_users(db), '------')
# print(User.get_user_info(db, User.get_all_users(db)))
# print(User.find_user(db, 'admin', '12345'), 444)


# d = datetime.date(2021, 11, 11)
# event = Event(db, d, 'kerman', 32, 32, 5)
# print(event.event_id)
# event.save()
# print(event.re_client.hmget(f"event:{event.event_id}:info", "place", 'date'))
# print(event.re_client.keys(pattern="event:*:info"))
# print(db.redis_client.hgetall("event:3:info"), 99999000)
# print(event.re_client.hmget(f"user:*:info", "type"))
# print(db.redis_client.hmget(f"event:9:info", 'place'), 999)
# print(User.get_all_users(db))
# t1 = Ticket(1)
