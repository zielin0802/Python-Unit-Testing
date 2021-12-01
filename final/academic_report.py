import sys

from CourseLoad import CourseLoad


def main():
    course_load = CourseLoad()
    course_load.load_raw_courseload_data('data/course_load.csv')
    course_load.load_courses_from_dataframe(course_load.raw_course_data)

    print(course_load.basic_info())
    print('\nAcademic History:')
    academic_history = course_load.academic_history()
    print(academic_history)
    course_load_file_name = course_load.save_academic_history(
        data=academic_history,
        output_dir='output'
    )
    print(f'\nSaved academic history report to {course_load_file_name}')


if __name__ == '__main__':
    sys.exit(main())
