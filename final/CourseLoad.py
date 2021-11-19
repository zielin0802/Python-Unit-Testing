class CourseLoad:
    def __init__(self):
        self.courses = dict()

    def __iter__(self):
        yield from self.courses.items()

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
