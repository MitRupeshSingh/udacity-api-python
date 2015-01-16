from nose.tools import *
from tests.test_user import *
import requests
import udacity


def test_key():
    '''Tests User.key'''

    user = udacity.User(USER, PW)
    assert type(user.key()) is str


def test_name():
    '''Tests User.name'''

    user = udacity.User(USER, PW)
    assert type(user.name()) is str


def test_nickname():
    '''Tests User.nickname'''

    user = udacity.User(USER, PW)
    assert type(user.nickname()) is str


def test_email():
    '''Tests User.email'''

    user = udacity.User(USER, PW)
    assert '@' in user.email()


def test_email_prefs():
    '''Tests User.email_preferences'''

    user = udacity.User(USER, PW)
    assert type(user.email_preferences()) is dict


def test_site_prefs():
    '''Tests User.site_preferences'''

    user = udacity.User(USER, PW)
    assert type(user.site_preferences()) is dict


def enrollments():
    '''Tests User.enrollments'''

    user = udacity.User(USER, PW)
    assert type(user.enrollments()) is list
    assert 'cs101' in user.enrollments()
