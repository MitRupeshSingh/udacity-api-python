from nose.tools import *
import udacity
import bx


def test_missing_args():
    '''Tests udacity.User with no args, when two are needed.'''

    assert_raises(TypeError, udacity.User)
    assert_raises(TypeError, udacity.User, 'hello')


def test_correct():
    '''Tests udacity.User with the correct number of arguments.'''

    user = udacity.User('name@example.com', 'password123')
    assert_dict_equal(user.creds, {
        'udacity': {
            'username': 'name@example.com',
            'password': 'password123'
        }
    })
    assert type(user.cache) is bx.Db
