from nose.tools import *
import udacity


def test_data_sci():
    '''Tests Catalog.track(name), with the "Data Science" track.'''

    catalog = udacity.Catalog()
    ds = catalog.track('Data Science')
    assert type(ds) is dict
    assert ds['name'] == "Data Science"


def test_malformed():
    '''Tests Catalog.track with a non-existant track name.'''

    catalog = udacity.Catalog()
    assert_raises(IndexError, catalog.track, 'aaaaaa')
