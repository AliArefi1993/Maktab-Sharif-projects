import datetime


def date_convert(date):
    date_format = datetime.datetime.strptime(date, "(%Y, %m, %d)")
    return date_format.strftime("%A-%B-%Y")


if __name__ == '__main__':
    print(date_convert("(2020, 5, 15)"))
