from collections import OrderedDict


def date_to_string(date, fmt='%m/%d/%Y'):
    return date.strftime(format=fmt)


class Course:
    def __init__(
        self, name=None, instructor=None, in_progress=False, units=3, grade=None,
        start_date=None, end_date=None
    ):
        self.name = name
        self.instructor = instructor
        self.in_progress = in_progress
        self.units = units
        self.grade = grade
        if grade is None and in_progress:
            self.grade = 'N/A'
        self.start_date = start_date
        self.end_date = end_date

        self.grade_points_map = OrderedDict({
            'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 'F': 0.0
        })
        for grade_symbol in ['I', 'P', 'NP', 'NR', 'NFC', 'Blank', 'N/A']:
            self.grade_points_map[grade_symbol] = None

    def grade_points(self):
        if self.grade in self.grade_points_map:
            return self.grade_points_map.get(self.grade)
        else:
            raise ValueError(
                f'Invalid grade: {self.grade}\nValid Grades: {list(self.grade_points_map.keys())}'
            )

    def season(self):
        if self.start_date:
            if self.start_date.month == 1:
                return 'Winter'
            elif self.start_date.month == 9:
                return 'Fall'
            elif self.start_date.month == 6:
                return 'Summer'
            elif self.start_date.month == 3:
                return 'Spring'
