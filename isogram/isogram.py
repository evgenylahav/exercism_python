def is_isogram(string: str) -> bool:
    """
    this function checks if string is an isogram or not
    :param string:
    :return: True is string is an isogram and False if it's not
    """
    unique_str = ''
    test_string = ''.join(x for x in string if x.isalpha())
    test_string = test_string.lower()
    for s in test_string:
        if s not in unique_str:
            unique_str = unique_str + s

    return unique_str == test_string


if __name__ == "__main__":
    print(is_isogram('Emily Jung Schwartzkopf'))
