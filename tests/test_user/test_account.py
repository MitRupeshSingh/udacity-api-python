from nose.tools import *
from tests.test_user import *
import requests
import udacity


def test_malformed():
    '''Tests User.account with bad user info.'''

    user = udacity.User('bad', 'data')
    assert_raises(requests.exceptions.HTTPError, user.account)


def test_legit():
    '''Tests User.account with actual data.'''

    user = udacity.User(USER, PW)
    data = user.account()
    assert data['first_name'] == 'Ty-Lucas'


def test_cache():
    '''Tests to make sure data is cached after the first request.'''

    user = udacity.User(USER, PW)
    data = user.account()
    assert user.cache.get('account') is not None
