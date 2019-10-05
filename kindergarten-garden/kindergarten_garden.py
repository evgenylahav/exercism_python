"""
Kindergarden garden maintenance
"""

from typing import List, Dict, Optional


class Garden(object):
    plants_names = {'G': 'Grass', 'V': 'Violets', 'C': 'Clover', 'R': 'Radishes'}
    student_names = ['Alice', 'Bob', 'Charlie', 'David',
                     'Eve', 'Fred', 'Ginny', 'Harriet',
                     'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram: str, students: Optional[List[str]]=None):
        """
        Create a student_gardens dict which holds mapping for each student
        and their planted plants
        """

        students = sorted(students or self.student_names)
        diagram = diagram.split('\n')

        self.student_gardens = self._parse_student_to_plants_list(students, diagram)

    def _parse_student_to_plants_list(self, students: List[str], diagram: List[str]) -> Dict[str, List[str]]:
        """
        Parse the students list and the diagram and
        create a dict assigning plants list per student name
        """

        student_to_plants = {}
        for index, student in enumerate(students):
            student_ind = index * 2
            student_diagram = diagram[0][student_ind:student_ind + 2] + \
                              diagram[1][student_ind:student_ind + 2]

            plants_per_student = []
            for plant in student_diagram:
                plants_per_student.append(self.plants_names[plant])

                student_to_plants[student] = plants_per_student

        return student_to_plants

    def plants(self, student: str) -> List[str]:
        """
        Get the name of the student and return the plants he/she planted
        """

        return self.student_gardens[student]
