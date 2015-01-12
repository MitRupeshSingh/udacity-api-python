import requests
import bx


class User():
    '''Log in and view account information and course progress.'''

    def __init__(self, email, password):
        '''
        Creates a new User instance.

        Args:
            email (str): User's email address
            password (str): User's password
        '''

        self.cache = bx.Db()
        self.creds = {
            'udacity': {
                'username': email,
                'password': password
            }
        }
        self.urls = {
            auth: 'https://www.udacity.com/api/session',
            account: 'https://www.udacity.com/api/users/me',
            node_progress: 'https://www.udacity.com/api/nodes/%s/state?fresh=true',
            node_info: 'https://www.udacity.com/api/nodes?keys%5B%5D=%s',
            classroom: 'https://www.udacity.com/course/viewer#!/'
        }

    def clear(self):
        '''Clears the cache.'''

        self.cache.clear()
