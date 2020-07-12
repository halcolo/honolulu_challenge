import unittest
import requests


class TestApi(unittest.TestCase):
    """Run main.py before start the test cases.
    """

    start_date = '2016-11-25'
    end_date = '2017-03-14'

    def rest_code(self, route):
        root = 'http://127.0.0.1:5000'
        result = requests.get(f'{root}{route}')
        return result.status_code

    def test_root(self):
        self.assertEqual(self.rest_code('/'), 200)

    def test_get_precipitation(self):
        self.assertEqual(self.rest_code('/api/v1.0/precipitation'), 200)

    def test_get_stations(self):
        self.assertEqual(self.rest_code('/api/v1.0/stations'), 200)

    def test_get_temp(self):
        self.assertEqual(self.rest_code(f'/api/v1.0/{self.start_date}'), 200)

    def test_get_temp(self):
        self.assertEqual(self.rest_code(f'/api/v1.0/{self.start_date}'), 200)

    def test_get_temp_start_end(self):
        self.assertEqual(self.rest_code(f'/api/v1.0/{self.start_date}/{self.end_date}'), 200)


if __name__ == '__main__':
    unittest.main()





