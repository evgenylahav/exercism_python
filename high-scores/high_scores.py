from typing import List


class HighScores(object):
    def __init__(self, scores: List[int]):
        self.scores = scores
        self._latest = scores[-1]
        self._personal_best = max(self.scores)
        self._sorted_list = sorted(self.scores, reverse=True)

    def latest(self) -> int:
        return self._latest

    def personal_best(self) -> int:
        return self._personal_best

    def personal_top(self) -> List[int]:
        return self._sorted_list[:3]

    def report(self) -> str:
        base_string = "Your latest score was {}. ".format(self._latest)
        last_best = "That's your personal best!"
        other_best = "That's {} short of your personal best!".format(self._personal_best - self._latest)

        if self._latest == self._personal_best:
            return base_string + last_best
        else:
            return base_string + other_best
