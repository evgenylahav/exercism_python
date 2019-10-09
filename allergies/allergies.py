import math


class Allergies(object):
    """
    Given a person's allergy score, determine whether or not they're allergic
    to a given item, and their full list of allergies.

    So if Tom is allergic to peanuts and chocolate, he gets a score of 34.
    Now, given just that score of 34, your program should be able to say:
        Whether Tom is allergic to any one of those allergens listed above.
        All the allergens Tom is allergic to.

    note: a given score may include allergens not listed. this program will ignore them
    """

    def __init__(self, score: int):
        self.score = score % 256
        self._lst = list()
        self.allergies_lst = dict()
        self.allergies_lst['eggs'] = 1
        self.allergies_lst['peanuts'] = 2
        self.allergies_lst['shellfish'] = 4
        self.allergies_lst['strawberries'] = 8
        self.allergies_lst['tomatoes'] = 16
        self.allergies_lst['chocolate'] = 32
        self.allergies_lst['pollen'] = 64
        self.allergies_lst['cats'] = 128

    def check_allergies(self):
        """
        this method will check the allergies based on the input score and will fill in the _lst
        property with the allergies that the subject has
        """
        while self.score > 0:
            p = math.floor(math.log2(self.score))
            allergy_score = 2 ** p
            for allergy, score in self.allergies_lst.items():
                if score == allergy_score:
                    self._lst.append(allergy)
            self.score -= allergy_score

    def is_allergic_to(self, item: str) -> bool:
        """
        this function will get an allergy and will return if the subject is allergic
        to that allergy or not
        """
        self.check_allergies()
        return item in self.lst

    @property
    def lst(self):
        """
        this property will hold the list of the allergies that the subject has based
        on his/her score
        """
        self.check_allergies()
        return self._lst
