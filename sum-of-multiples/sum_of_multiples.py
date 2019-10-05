from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    """
    Given a number, find the sum of all the unique multiples of
    particular numbers up to but not including that number.
    example:
    sum_of_multiples(6, [4])
    -> 4
    sum_of_multiples(20, [3, 5])
    -> 78
    """
    unique_multiples: List[int] = []
    for num in range(limit):
        if any(num % x == 0 for x in multiples):
            unique_multiples.append(num)

    return sum(unique_multiples)
