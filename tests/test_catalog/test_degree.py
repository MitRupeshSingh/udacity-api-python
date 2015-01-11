from nose.tools import *
import udacity


def test_nd001():
    '''Tests Catalog.degree(key), using nd001.'''

    catalog = udacity.Catalog()
    nd = catalog.degree('nd001')
    assert type(nd) is dict
    assert nd['key'] == 'nd001'


def test_malformed():
    '''Tests Catalog.degree with a fake key.'''

    catalog = udacity.Catalog()
    assert_raises(IndexError, catalog.degree, 'aaaaaaa')
