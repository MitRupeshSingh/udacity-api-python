from nose.tools import *
from tests.test_user import *
import requests
import udacity


def test_progress():
    '''Tests User.progress'''

    user = udacity.User(USER, PW)
    prog = user.progress('cs101')
    assert type(prog) is dict

    keys = [
        'title',
        'key',
        'completed',
        'current_lesson',
        'morsel_count',
        'last_visited',
        'morsels_completed',
        'most_recent_url',
        'quiz_count',
        'quizzes_completed',
        'time_away_ms'
    ]

    for k in keys:
        assert k in prog

    assert type(prog['current_lesson']) is dict


def test_progress_malformed():
    '''Tests User.progress with a nonexistant course key.'''

    user = udacity.User(USER, PW)
    assert_raises(IndexError, user.progress, 'aaaaaaa')
