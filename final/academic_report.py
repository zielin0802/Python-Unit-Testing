import sys

from CourseLoad import CourseLoad


def main():
    course_load = CourseLoad()
    course_load.load_raw_courseload_data('data/course_load.csv')
    course_load.load_courses_from_dataframe(course_load.raw_course_data)

    print(course_load.basic_info())


if __name__ == '__main__':
    sys.exit(main())
