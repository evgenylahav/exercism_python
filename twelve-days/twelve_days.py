from typing import List

DAYS = ["first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
PRESENTS = ["a Partridge in a Pear Tree",
            "two Turtle Doves",
            "three French Hens",
            "four Calling Birds",
            "five Gold Rings",
            "six Geese-a-Laying",
            "seven Swans-a-Swimming",
            "eight Maids-a-Milking",
            "nine Ladies Dancing",
            "ten Lords-a-Leaping",
            "eleven Pipers Piping",
            "twelve Drummers Drumming"]


def recite(start_verse: int, end_verse: int) -> List[str]:
    verses = range(start_verse, end_verse + 1)
    song = []
    for verse in verses:
        song.append("On the {} day of Christmas my true love gave to me: ".format(DAYS[verse - 1]))
        for i in range(verse, 0, -1):
            if i == 1 and verse == 1:
                song[-1] += '{}.'.format(PRESENTS[i-1])
            elif i == 1:
                song[-1] += 'and {}.'.format(PRESENTS[i-1])
            else:
                song[-1] += '{}, '.format(PRESENTS[i-1])
    return song
