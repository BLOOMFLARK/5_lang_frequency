import sys
from collections import Counter
import re


def load_data(file_path):
    try:
        file = open(file_path, 'r')
        return file.read()

    except FileNotFoundError:
        return None


def prepared_text(text):
    return [word for word in re.findall(r'\w+', text.lower())]


def get_most_frequent_words(text, number_of_words):
    words = prepared_text(text)
    counter = Counter(words)
    return counter.most_common(number_of_words)


def print_most_frequent_words(words_data):
    for word in words_data:
        print(word[0])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        sys.exit('no file path')
    text = load_data(file_path)

    if not text:
        sys.exit('file not found')
    else:
        print_most_frequent_words(get_most_frequent_words(text, number_of_words=10))
