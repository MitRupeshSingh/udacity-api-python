from requests.exceptions import HTTPError
from nose.tools import *
import udacity


def test_get():
    '''Tests Catalog.__get.'''

    catalog = udacity.Catalog()
    assert type(catalog.all()) is dict


def test_get_malformed():
    '''Tests Catalog.__get, with the wrong URL.'''

    catalog = udacity.Catalog()
    catalog.url = 'https://www.udacity.com/fake'

    assert_raises(HTTPError, catalog.all)
