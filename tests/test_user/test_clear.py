from nose.tools import *
from tests.test_user import *
import udacity


def test_empty():
    '''Tests User.clear with no existing data.'''

    user = udacity.User(USER, PW)
    assert_dict_equal(user.cache.data, {})
    user.clear()
    assert_dict_equal(user.cache.data, {})


def test_filled():
    '''Tests User.clear with existing data.'''

    user = udacity.User(USER, PW)
    assert_dict_equal(user.cache.data, {})
    courses = user.enrollments()
    assert user.cache.data.get('account') is not None
    user.clear()
    assert_dict_equal(user.cache.data, {})
