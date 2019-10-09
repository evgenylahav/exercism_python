def reverse(text: str) -> str:
    """
    this function will reverse the input string
    :param text:
    :return: reversed text
    """
    rev_text = ""
    for s in text:
        rev_text = s + rev_text
    return rev_text


if __name__ == "__main__":
    print(reverse('dwarf'))
