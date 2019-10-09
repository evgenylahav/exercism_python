import re
from collections import Counter


def word_count(phrase: str) -> Counter:
    phrase = re.sub('_', ' ', phrase)
    words = re.findall(r"[\w']+|[_]", phrase.lower())

    return Counter([word.strip("'") for word in words])
