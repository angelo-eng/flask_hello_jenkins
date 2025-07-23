import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_new_route(self):
        rv = self.app.get('/feature/test')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
