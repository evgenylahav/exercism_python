class Luhn(object):
    def __init__(self, card_num: str):
        self.card_number = card_num.replace(" ", "")[::-1]

    def is_valid(self) -> bool:
        if len(self.card_number) <= 1 or not self.card_number.isnumeric():
            return False

        doubled_number = ""
        for counter, num_val in enumerate(self.card_number):
            doubled_number += self._get_next_num(counter, num_val)

        return sum([int(n) for n in doubled_number]) % 10 == 0

    @staticmethod
    def _get_next_num(counter: int, num_val: str) -> str:
        if counter % 2 == 1:
            n = int(num_val) * 2
            if n > 9:
                n -= 9
            num_val = str(n)

        return num_val
