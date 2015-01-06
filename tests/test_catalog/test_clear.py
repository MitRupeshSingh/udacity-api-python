from nose.tools import *
import udacity


def test_empty():
    '''Tests Catalog.clear with no existing data.'''

    catalog = udacity.Catalog()
    assert_dict_equal(catalog.cache.data, {})
    catalog.clear()
    assert_dict_equal(catalog.cache.data, {})


def test_filled():
    '''Tests Catalog.clear with existing data.'''

    catalog = udacity.Catalog()
    assert_dict_equal(catalog.cache.data, {})
    courses = catalog.all()
    assert catalog.cache.data.get('catalog') is not None
    catalog.clear()
    assert_dict_equal(catalog.cache.data, {})
