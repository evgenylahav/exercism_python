def setup_dict(book):
    table = {}
    for word in book.split():
        word = word.lower()
        if word in table:
            table[word] += 1
        else:
            table[word] = 1
    return table


def get_frequency(table, word):
    return table[word.lower()]


book = 'ak ak rfrfrfkffc ak dfgv'
table = setup_dict(book)
word = 'aK'
print(get_frequency(table, word))