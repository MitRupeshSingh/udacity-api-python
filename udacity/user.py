from datetime import datetime as dt
import requests
import json
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
        self.session = requests.Session()
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.creds = {
            'udacity': {
                'username': email,
                'password': password
            }
        }
        self.urls = {
            'auth': 'https://www.udacity.com/api/session',
            'account': 'https://www.udacity.com/api/users/me',
            'node_prog': 'https://www.udacity.com/api/nodes/%s/state?fresh=true',
            'node_info': 'https://www.udacity.com/api/nodes?keys%5B%5D=%s',
            'classroom': 'https://www.udacity.com/course/viewer#!/'
        }

    def clear(self):
        '''Clears the cache.'''

        self.cache.clear()

    def __auth(self):
        '''
        Checks if a user is logged in; if not, log them in.

        Returns:
            dict: Session data

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        try:
            return self.cache.get('session')
        except KeyError:
            req = self.session.post(self.urls['auth'], data=json.dumps(self.creds),
                                    headers=self.headers)
            req.raise_for_status()

            data = json.loads(req.text[4:])
            self.cache.put('session', data)
            return data

    def account(self):
        '''
        Get all account data for a user.

        Returns:
            dict: User account info

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        try:
            return self.cache.get('account')
        except KeyError:
            try:
                self.cache.get('session')
            except KeyError:
                self.__auth()

            req = self.session.get(self.urls['account'])
            req.raise_for_status()

            data = json.loads(req.text[4:])['user']
            self.cache.put('account', data)
            return data

    def key(self):
        '''
        Get a user's Udacity ID.

        Returns:
            str: User's ID

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.account()
        return data['key']

    def name(self):
        '''
        Get a user's name.

        Returns:
            str: User's name

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.account()
        return data['first_name'] + ' ' + data['last_name']

    def nickname(self):
        '''
        Get a user's nickname.

        Returns:
            str: User's nickname

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.account()
        return data['nickname']

    def email(self):
        '''
        Get a user's email address.

        Returns:
            str: User's email

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.account()
        return data['email']['address']

    def email_preferences(self):
        '''
        Get a user's preferences for things like newsletters, class emails, etc.

        Returns:
            dict: User's email preferences

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.account()
        return {
            'employer_sharing': data['employer_sharing'],
            'newsletter': data['email_preferences']['master_ok'],
            'course_emails': data['email_preferences']['ok_course'],
            'user_research': data['email_preferences']['ok_user_research']
        }

    def site_preferences(self):
        '''
        Get a user's preferences for things like video quality and playback.

        Returns:
            dict: User's site preferences

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.account()
        return data['site_preferences']

    def enrollments(self):
        '''
        Get the ID's of courses a user is enrolled in.

        Returns:
            list: List of courses enrolled in

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.account()
        return [course['node_key'] for course in data['_enrollments']]

    def progress(self, key):
        '''
        Get progress in one course.

        Args:
            key (str): Course ID

        Returns:
            dict: Info about a course

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
            IndexError: If user is not enrolled in the requested course
        '''

        def get_course_progress():
            req = self.session.get(self.urls['node_prog'] % key)
            req.raise_for_status()

            course_progress = json.loads(req.text[4:])['nodestates'][0]

            most_recent_page = course_progres['last_interactions'].sort(key=lambda i: dt.strptime(i.time, '%Y-%m-%dT%H:%M:%S.%fZ'))[0]

        try:
            return self.cache.get(key)
        except KeyError:
            courses = self.enrollments()
            if key not in courses:
                raise IndexError('User not enrolled in course ' + str(key))
            else:
                return get_course_progress()
