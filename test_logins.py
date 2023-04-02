
import unittest
from TA_api import app, db,  create_user
import json


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        create_user('sona', 'password@123')
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = 'sona'"
        cursor.execute(query)
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        cursor.execute("DELETE FROM users WHERE username = 'sona'")
        db.commit()

    def test_login_success(self):
        username = 'sona'
        password = 'password@123'
        create_user(username, password)
        response = self.app.post(
            '/login', json={'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)
        db.commit()

    def test_login_fail(self):
        username = 'sti'
        password = ''
        create_user(username, 'wrong_password')
        response = self.app.post(
            '/login', json={'username': username, 'password': password})
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
