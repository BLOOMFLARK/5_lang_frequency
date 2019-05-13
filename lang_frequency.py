import sys


def load_data(file_path):
    try:
        f = open(file_path, 'r')
        return f.read()

    except FileNotFoundError:
        return None


def get_most_frequent_words(words):
    counted_words = {}
    for word in words:
        if not counted_words.get(word):
            counted_words[word] = 1
        else:
            counted_words[word] += 1

    counted_words_list = list(counted_words.items())
    sorted_counted_words_list = sorted(counted_words_list, key=lambda x: x[1], reverse=True)
    if len(text) < 10:
        return sorted_counted_words_list
    else:
        return sorted_counted_words_list[0:10]


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
        print_most_frequent_words(get_most_frequent_words(text.split(' ')))
