import datetime

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
            'start_date': datetime.date(year=2021, month=1, day=12),
            'end_date': datetime.date(year=2021, month=3, day=9)
        }
    ])
