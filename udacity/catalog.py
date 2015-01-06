import requests
import bx


class Catalog():
    '''A wrapper over the Udacity Catalog API.'''

    def __init__(self):
        '''Creates a new catalog to interact with.'''

        self.cache = bx.Db()
        self.url = 'https://www.udacity.com/public-api/v0/courses?projection=internal'

    def clear(self):
        '''Clear all stored catalog data.'''

        self.cache.clear()

    def __get(self):
        '''
        Get and cache catalog data from Udacity's website.

        Returns:
            dict: The entire course catalog

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        try:
            return self.cache.get('catalog')
        except KeyError:
            req = requests.get(self.url)
            req.raise_for_status()

            data = req.json()
            self.cache.put('catalog', data, timeout=60000)
            return data

    def all(self):
        '''
        Get the entire catalog.

        Returns:
            dict: The entire catalog

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.__get()
        return data

    def courses(self):
        '''
        Get the courses portion of the catalog.

        Returns:
            list of dict: All course data

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.__get()
        return data.get('courses')

    def course(self, key):
        '''
        Get the data for one course.

        Args:
            key (str): The course ID

        Returns:
            dict: The course data

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
            IndexError: If no course that matches the key is found
        '''

        data = self.__get()
        return [x for x in data['courses'] if x['key'] == key][0]

    def instructors(self, key):
        '''
        Get instructor information for a course.

        Args:
            key (str): The course ID

        Returns:
            list of dict: Info on each instructor in the course

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.course(key)
        return data.get('instructors')

    def tracks(self):
        '''
        Get all tracks.

        Returns:
            list of dict: All tracks

        Raises:
            requests.exceptions.HTTPError: If page is not found or server error
        '''

        data = self.__get()
        return data.get('tracks')
