from typing import Tuple


class Clock:
    def __init__(self, hours: int, minutes: int):
        self.hours, self.minutes = self.rounding_clock(hours, minutes)

    def __str__(self) -> str:
        return '{:02d}:{:02d}'.format(self.hours, self.minutes)

    def __add__(self, other):
        hours, minutes = self.rounding_clock(self.hours, self.minutes + other)
        return self.__class__(hours, minutes)

    def __sub__(self, other):
        hours, minutes = self.rounding_clock(self.hours, self.minutes - other)
        return self.__class__(hours, minutes)

    def __eq__(self, other):
        other_hours, other_minutes = self.rounding_clock(other.hours, other.minutes)
        return self.hours == other_hours and self.minutes == other_minutes

    @staticmethod
    def rounding_clock(hours: int, minutes: int) -> Tuple[int, int]:
        rounded_hours = (hours % 24 + minutes // 60) % 24
        rounded_minutes = minutes % 60
        return rounded_hours, rounded_minutes
