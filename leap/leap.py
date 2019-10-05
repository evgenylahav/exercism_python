
def is_num_div_by_val(num: int, divider: int) -> bool:
    """
    this function gets an int number and an int divider and returns True if the number
    is divided by the divider without a remainder and False if the number is divided
    by the divider with a reminder
    :param num: the examined number
    :param divider: the examined divider
    :return: True / False
    """
    if divider == 0:
        raise Exception("Can't divide by zero. Please use another divider.")
    return num % divider == 0


def is_leap_year(year: int) -> bool:
    """
    this function checks if the input year is a leap year by the following logic:
    every year that is evenly divisible by 4
      except every year that is evenly divisible by 100
          unless the year is also evenly divisible by 400
    :param year: the examined year [int]
    :return: True / False
    """
    if not isinstance(year, int):
        raise Exception("Must use integer inputs only!")
    return is_num_div_by_val(year, 4) and \
           (not is_num_div_by_val(year, 100) or is_num_div_by_val(year, 400))


if __name__ == '__main__':
    test_year = '344'
    print(is_leap_year(test_year))
