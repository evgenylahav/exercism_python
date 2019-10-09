from collections import Counter

PRICE = 800
DISCOUNTS = {1: 0, 2: 5, 3: 10, 4: 20, 5: 25}


def total(books):
    if not books:
        return 0

    book_groups = split_books_to_groups(Counter(books))
    book_groups = prepare_for_calculation(book_groups)
    discounts = [DISCOUNTS[len(counter + Counter())] for counter in book_groups]
    return sum([sum(counter.values()) * PRICE * (1 - discount / 100)
                for counter, discount in zip(book_groups, discounts)])


def split_books_to_groups(counter):
    result = []
    new_counter = Counter()
    if max(counter.values()) > 1:
        counter_sorted = counter.most_common()
        for book, amount in counter_sorted:
            if amount >= 2 < 4:
                new_counter[book] += 1
                counter[book] -= 1

        result.append(split_books_to_groups(counter))
    else:
        result = counter

    if new_counter:
        result.append(new_counter)

    return result


def prepare_for_calculation(book_groups):
    if not isinstance(book_groups, list):
        result = [book_groups]
    else:
        f = Flatter()
        f.parse_nested_list(book_groups)
        result = f.output

    # change the distribution
    result = re_arrange(result)

    return result


def re_arrange(list_of_c):
    ind_5 = [i for i, x in enumerate(list_of_c) if len(x) == 5]
    ind_3 = [i for i, x in enumerate(list_of_c) if len(x) == 3]

    min_re_arrangement = min(len(ind_5), len(ind_3))

    for i in range(min_re_arrangement):
        keys = list(list_of_c[ind_5[i]].keys() - list_of_c[ind_3[i]].keys())
        list_of_c[ind_3[i]][keys[0]] += 1
        list_of_c[ind_5[i]][keys[0]] -= 1

    return list_of_c


class Flatter:
    def __init__(self):
        self.output = []

    def parse_nested_list(self, l):
        for i in l:
            if type(i) == list:
                self.parse_nested_list(i)
            else:
                self.output.append(i)
