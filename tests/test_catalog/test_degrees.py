from nose.tools import *
import udacity


def test():
    '''Tests Catalog.degrees.'''

    catalog = udacity.Catalog()
    degrees = catalog.degrees()
    assert type(degrees) is list
    assert [x for x in degrees if x['key'] == 'nd001'][0] is not None
