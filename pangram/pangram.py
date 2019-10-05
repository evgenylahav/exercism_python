"""
this module tests a given phrase to see if it is a pangram
A pangram is a sentence using every letter of the alphabet at least once.
The best known English pangram is:
The quick brown fox jumps over the lazy dog.

The alphabet used consists of ASCII letters a to z, inclusive, and is case insensitive.
Input will not contain non-ASCII symbols.
"""

import string
from typing import List


def get_alphabet() -> List:
    """
    this function creates a list of the english alphabet letters in lower case
    :return: list of lower case letters of the alphabet
    """
    return list(string.ascii_lowercase)

def is_pangram(sentence: str) -> bool:
    """
    this function checks whether the input sentence is a panagram
    :param sentence: a string of letters
    :return: True / False
    """
    alphabet = get_alphabet()
    test_list = [False] * len(alphabet)
    for letter in sentence:
        if letter.isalpha():
            test_list[alphabet.index(letter.lower())] = True

    return all(test_list)


if __name__ == '__main__':
    TEST_SENTENCE = 'the 1 quick brown fox jumps over the 2 lazy dogs'
    print(is_pangram(TEST_SENTENCE))