def is_armstrong(number: int) -> bool:
    str_number = str(number)
    return sum(int(a) ** len(str_number) for a in str_number) == number
