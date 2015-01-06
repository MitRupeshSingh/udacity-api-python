from nose.tools import *
import udacity


def test():
    '''Tests Catalog.tracks.'''

    catalog = udacity.Catalog()
    assert type(catalog.tracks()) is list
    assert type(catalog.tracks()[0]['name']) is str
