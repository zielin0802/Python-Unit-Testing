from datetime import date
import pytest

from Course import Course, date_to_string


@pytest.fixture
def course():
    return Course()


@pytest.fixture
def course_with_init_data(course):
    return Course(
        name='Python Unit Testing',
        instructor='Shivakumar Mathapathi',
        in_progress=True,
        units=3,
        grade='N/A',
        start_date=date(year=2021, month=9, day=28),
        end_date=date(year=2021, month=11, day=30)
    )


def test_date_to_string():
    assert date_to_string(date(1981, 8, 2)) == '08/02/1981'


def test_course_init_defaults(course):
    assert course.name is None
    assert course.instructor is None
    assert course.in_progress is False
    assert course.units == 3
    assert course.grade is None
    assert course.start_date is None
    assert course.end_date is None


def test_course_init_with_params(course_with_init_data):
    assert course_with_init_data.name == 'Python Unit Testing'
    assert course_with_init_data.instructor == 'Shivakumar Mathapathi'
    assert course_with_init_data.in_progress
    assert course_with_init_data.units == 3
    assert course_with_init_data.grade == 'N/A'
    assert course_with_init_data.start_date == date(year=2021, month=9, day=28)
    assert course_with_init_data.end_date == date(year=2021, month=11, day=30)


def test_init_course_in_progress_grade_na():
    c = Course(in_progress=True)
    assert c.grade == 'N/A'
    assert c.grade_points() is None


def test_course_assignment(course):
    course.name = 'Data Analytics Using Python'
    course.instructor = 'Shivakumar Mathapathi'
    course.in_progress = False
    course.units = 3
    course.grade = 'A+'

    assert course.name == 'Data Analytics Using Python'
    assert course.instructor == 'Shivakumar Mathapathi'
    assert course.in_progress is False
    assert course.units == 3
    assert course.grade == 'A+'


@pytest.mark.parametrize(
    'grade, points',
    [('A+', 4.0), ('A', 4.0), ('B-', 2.7), ('C', 2.0), ('F', 0.0), ('I', None)]
)
def test_grade_points(course, grade, points):
    course.grade = grade
    assert course.grade_points() == points


def test_grade_points_invalid_grade(course):
    course.grade = 'C++'
    with pytest.raises(ValueError):
        course.grade_points()

    course.grade = 'C#'  # do re mi fa so la ti do while
    with pytest.raises(ValueError):
        course.grade_points()


def test_season_no_start_date(course):
    assert course.season() is None


def test_season_with_start_date(course_with_init_data):
    assert course_with_init_data.season() == 'Fall'
    # TODO: add other 3 seasons
