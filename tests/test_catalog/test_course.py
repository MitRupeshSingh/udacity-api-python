from nose.tools import *
import udacity


def test_cs101():
    '''Tests Catalog.course('cs101').'''

    catalog = udacity.Catalog()
    assert type(catalog.course('cs101')) is dict
    assert len(catalog.course('cs101')) == 34
    assert catalog.course('cs101').get('key') == 'cs101'


def test_invalid():
    '''Tests Catalog.course with an invalid key.'''

    catalog = udacity.Catalog()
    assert_raises(IndexError, catalog.course, 'fake_course_key')
