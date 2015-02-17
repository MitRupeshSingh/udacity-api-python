from nose.tools import *
from tests.test_user import *
import requests
import udacity


def test_progress():
    '''Tests User.progress'''

    user = udacity.User(USER, PW)
    prog = user.progress('cs101')
    assert type(prog) is dict
    assert type(prog['current_lesson']) is dict

    keys = [
        'key',
        'title',
        'quiz_count',
        'morsel_count',
        'completed',
        'quizzes_completed',
        'morsels_completed',
        'last_visited',
        'time_away_ms',
        'most_recent_url',
        'current_lesson'
    ]

    for k in keys:
        assert k in prog


def test_progress_malformed():
    '''Tests User.progress with a nonexistant course key.'''

    user = udacity.User(USER, PW)
    assert_raises(IndexError, user.progress, 'aaaaaaa')
