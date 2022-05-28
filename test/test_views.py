import unittest
from hello_world import app
from hello_world.formatter import SUPPORTED

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config('TESTING') = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_mgs_with_output(self):
        rv = self.app.get('/output=json')
        self.assertEqual(b'{imie: "Natalia", "msg": Hello world!""}', rv.data)
