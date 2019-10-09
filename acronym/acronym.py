import re


def abbreviate(words: str) -> str:
    """ get a phrase and return its acronym """
    # use regex to find all words that start with letters
    words_lst = re.findall(r"[\w']+", words)
    return ''.join([word[0].upper() for word in words_lst])
