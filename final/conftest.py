import pandas as pd
import pytest


@pytest.fixture
def course_load_dataframe():
    return pd.DataFrame([
        {
            'section_id': 152524,
            'course_id': 'CSE-41273',
            'instructor': 'Diane Chen',
            'name': 'Python Programming Fundamentals',
            'units': 3,
            'grade': 'A+',
            'start_date': '1/12/21',
            'end_date': '3/9/21',
            'fee': 695
        }
    ])
