from datetime import datetime
import os

from Course import Course

import pandas as pd


def mkdir_if_not_exists(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


class CourseLoad:
    def __init__(self):
        self.courses = dict()
        self.raw_course_data = None
        self.date_format = '%m/%d/%y'

    def __iter__(self):
        yield from self.courses.items()

    def load_raw_courseload_data(self, input_file_name):
        self.raw_course_data = pd.read_csv(input_file_name)

    def load_courses_from_dataframe(self, data):
        for row in data.itertuples():
            self.courses[row.section_id] = Course(
                section_id=row.section_id,
                course_id=row.course_id,
                name=row.name,
                instructor=row.instructor,
                units=row.units,
                grade=row.grade,
                start_date=datetime.strptime(row.start_date, self.date_format),
                end_date=datetime.strptime(row.end_date, self.date_format),
                fee=row.fee
            )

    def gpa(self):
        try:
            graded_courses = [
                course
                for _, course in self
                if course.grade_points() is not None
            ]
        except ValueError as ve:
            raise ValueError(f'Can only calculate GPA with valid grades.\n{ve}')
        graded_courses_count = len(graded_courses)
        if graded_courses_count > 0:
            grade_points = [course.grade_points() for course in graded_courses]
            return sum(grade_points) / graded_courses_count

    def total_fees(self):
        return sum([course.fee for _, course in self])

    def basic_info(self):
        fees_string = '${:,.2f}'.format(self.total_fees())
        gpa_string = '{:.2f}'.format(self.gpa())
        attributes = [
            f'Total Courses: {len(self.courses)}',
            f'Total Fees: {fees_string}',
            f'GPA: {gpa_string}'
        ]

        return '\n'.join(attributes)

    def academic_history(self):
        card = self.raw_course_data[['section_id', 'name', 'grade', 'start_date', 'end_date']].copy()
        card['season'] = card.apply(
            lambda row: self.courses[row.section_id].season(), axis=1
        )
        card['year'] = card.apply(
            lambda row: self.courses[row.section_id].start_date.year, axis=1
        )
        card['month'] = card.apply(
            lambda row: self.courses[row.section_id].start_date.month, axis=1
        )
        card = card.sort_values(by=['year', 'month'])
        card.columns = [column_name.capitalize() for column_name in card.columns]

        return card[['Year', 'Season', 'Name', 'Grade']]

    def save_academic_history(self, data, output_dir, output_file_name='academic_history.csv'):
        mkdir_if_not_exists(output_dir)
        full_output_file_name = os.path.join(output_dir, output_file_name)
        data.to_csv(full_output_file_name)

        return full_output_file_name
