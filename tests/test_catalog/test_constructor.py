from nose.tools import *
import udacity


def test():
    '''Tests Catalog.__init__ with default options.'''

    catalog = udacity.Catalog()
    assert_dict_equal(catalog.cache.data, {})
    assert catalog.url == 'https://www.udacity.com/public-api/v0/courses?projection=internal'
