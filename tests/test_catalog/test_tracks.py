from nose.tools import *
import udacity


def test():
    '''Tests Catalog.tracks.'''

    catalog = udacity.Catalog()
    assert type(catalog.tracks()) is list
    tracks = catalog.tracks()
    assert tracks[0].get('name') is not None
