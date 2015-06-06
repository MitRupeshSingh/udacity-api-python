from nose.tools import *
import udacity


def test_courses():
    '''Tests Catalog.courses.'''

    catalog = udacity.Catalog()
    courses = catalog.courses()
    assert type(courses) is list
    assert len(courses[0]) == 34

    keys = [
        'instructors',
        'subtitle',
        'key',
        'image',
        'syllabus',
        'assistants',
        'summary',
        'starter'
    ]

    for k in keys:
        assert k in courses[0]
