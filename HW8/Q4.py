import re


def check_special_character(text):
    x = re.search('(A)?.=*([0-9])?.=*([$])', text)
    if x:
        return True
    return False


if __name__ == '__main__':
    print(check_special_character("Ao5$il"))
