import re


def search_word_end(text, word):
    x = re.search(f'{word}$', text)
    return x


if __name__ == '__main__':
    print(search_word_end("ali", "i"))
