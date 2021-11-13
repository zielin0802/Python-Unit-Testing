"""Module for reprsenting an academic course."""

import sys


def date_to_string(date, fmt='%m/%d/%Y'):
    """Convert date object to string.format

    :param date: (datetime.date, datetime.datetime)
    :param fmt: str: format of return string
    :return str:
    """
    return date.strftime(format=fmt)


class Course:
    """Class defintion for Course."""
    def __init__(
        self, name=None, instructor=None, in_progress=False, units=3, grade=None,
        start_date=None, end_date=None
    ):
        """Initialize Course object.

        :param name: str: name of the course
        :param instructor: str: instructor full name
        :param in_progress: bool: Is the course in progress?
        :param units: int
        :param grade: (int, float)
        :param start_date: (datetime.date, datetime.datetime)
        :param end_date: (datetime.date, datetime.datetime)
        """
        self.name = name
        self.instructor = instructor
        self.in_progress = in_progress
        self.units = units
        self.grade = grade
        if grade is None and in_progress:
            self.grade = 'N/A'
        self.start_date = start_date
        self.end_date = end_date
        self._grade_points_map = {
            'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 'F': 0.0
        }
        if sys.version_info.major >= 3 and sys.version_info.minor >= 7:
            self.grade_points_map = self._grade_points_map
        else:
            from collections import OrderedDict
            self.grade_points_map = OrderedDict(self._grade_points_map)

        for grade_symbol in ['I', 'P', 'NP', 'NR', 'NFC', 'Blank', 'N/A']:
            self.grade_points_map[grade_symbol] = None

    def grade_points(self):
        """Return grade points from this course letter grade.

        :returns float:
        :raises ValueError: if self.grade is not a valid letter grade.
        """
        if self.grade in self.grade_points_map:
            return self.grade_points_map.get(self.grade)
        else:
            raise ValueError(
                f'Invalid grade: {self.grade}\nValid Grades: {list(self.grade_points_map.keys())}'
            )

    def season(self):
        """Return season in which the course occurs, based on start date.
        """
        if self.start_date:
            if self.start_date.month in [12, 1, 2]:
                return 'Winter'
            elif self.start_date.month in [3, 4, 5]:
                return 'Spring'
            elif self.start_date.month in [6, 7, 8]:
                return 'Summer'
            elif self.start_date.month in [9, 10, 11]:
                return 'Fall'
