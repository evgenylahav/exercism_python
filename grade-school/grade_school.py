"""
Given students' names along with the grade that they are in,
create a roster for the school.
The class can:
1. Add a student's name to the roster for a grade
2. Get a list of all students enrolled in a grade
3. Get a sorted list of all students in all grades
"""

from typing import List


class School(object):
    def __init__(self):
        self.school_grade = [[]]

    def add_student(self, name: str, grade: int) -> None:
        """
        Add a student name to a roster of a grade
        This method updates the school_grade list of lists property
        """
        try:
            self.school_grade[grade-1].append(name)
        except IndexError:
            for i in range(len(self.school_grade), grade):
                self.school_grade.append([])
            self.school_grade[grade - 1].append(name)

    def roster(self) -> List[str]:
        """
        Return a flat list of all students sorted by grade first and then by name
        """

        return [item for sublist in self.school_grade for item in sorted(sublist)]

    def grade(self, grade_number: int):
        """
        Return the roster of a grade
        """
        return sorted(self.school_grade[grade_number - 1])
