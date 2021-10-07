import re


def check_phone_number(number):
    if re.search(r"^(\+98|00|0|098|\+098|\+0|\+0098)9\d{9}$", number):
        return True
    return False


if __name__ == '__main__':
    print(check_phone_number("0930160568994"))
