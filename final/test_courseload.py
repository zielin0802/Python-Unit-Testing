import pytest

from Course import Course
from CourseLoad import CourseLoad


@pytest.fixture
def course_load():
    return CourseLoad()


def test_courseload_init_defaults(course_load):
    assert isinstance(course_load.courses, dict)
    assert len(course_load.courses.keys()) == 0


def test_course_load_iter(course_load):
    course_load.courses['123'] = Course(name='Python Unit Testing')
    course_load.courses['ABC'] = Course(units=4)

    course_load_iter = iter(course_load)

    course_id, course_obj = next(course_load_iter)
    assert course_id == '123'
    assert course_obj.name == 'Python Unit Testing'

    course_id, course_obj = next(course_load_iter)
    assert course_id == 'ABC'
    assert course_obj.units == 4

    with pytest.raises(StopIteration):
        next(course_load_iter)


def test_gpa_valid_grades(course_load):
    course_load.courses[0] = Course(grade='A+')
    course_load.courses['1'] = Course(grade='B')
    course_load.courses['222222'] = Course(grade='N/A')
    course_load.courses[3] = Course(grade='C')
    assert course_load.gpa() == 3.0


def test_gpa_missing_grade(course_load):
    course_load.courses[0] = Course(grade='A+')
    course_load.courses['1'] = Course()
    with pytest.raises(ValueError):
        course_load.gpa()


def test_gpa_invalid_grade(course_load):
    course_load.courses[0] = Course(grade='C+')
    course_load.courses['1'] = Course(grade='Java')
    with pytest.raises(ValueError):
        course_load.gpa()


def test_gpa_no_grades(course_load):
    assert course_load.gpa() is None
