from Course import Course


class CourseLoad:
    def __init__(self):
        self.courses = dict()

    def __iter__(self):
        yield from self.courses.items()

    def load_courses_from_dataframe(self, data):
        for row in data.itertuples():
            self.courses[row.section_id] = Course(
                section_id=row.section_id,
                course_id=row.course_id,
                name=row.name,
                instructor=row.instructor,
                units=row.units,
                grade=row.grade,
                start_date=row.start_date,
                end_date=row.end_date
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
