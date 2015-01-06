from nose.tools import *
import udacity


def test_cs101():
    '''Tests Catalog.instructors('cs101').'''

    catalog = udacity.Catalog()
    i = catalog.instructors('cs101')
    assert type(i) is list
    assert len(i[0]) is 4
    assert set(i[0].keys()) == {'bio', 'image', 'name', 'key'}


def test_fake():
    '''Tests Catalog.instructors, with a fake course key.'''

    catalog = udacity.Catalog()
    assert_raises(IndexError, catalog.instructors, 'fake')
