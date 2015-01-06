from nose.tools import *
import udacity


def test_all():
    '''Tests Catalog.all.'''

    catalog = udacity.Catalog()
    assert set(catalog.all().keys()) == {'courses', 'tracks', 'degrees'}
