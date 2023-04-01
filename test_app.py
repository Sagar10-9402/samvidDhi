

import unittest
import json
from api import app , jwt_token 

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.jwt_token = jwt_token
        
    def test_create_ta(self):
        data = {
            "native_english_speaker": True,
            "course_instructor": "John Smith",
            "course": "Computer Science",
            "semester": 1,
            "class_size": 30,
            "class_attribute": "Introductory"
        }
        headers = {
            "Authorization": f"Bearer {self.jwt_token}"
        }
        response = self.app.post('/ta', data=json.dumps(data), headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        
    def test_retrieve_ta(self):
        headers = {
            "Authorization": f"Bearer {self.jwt_token}"
        }
        response = self.app.get('/ta/4', headers=headers)
        self.assertEqual(response.status_code, 200)
        
    def test_update_ta(self):
        data = {
            "native_english_speaker": False,
            "course_instructor": "Jane Doe",
            "course": "Mathematics",
            "semester": 2,
            "class_size": 20,
            "class_attribute": "Advanced"
        }
        headers = {
            "Authorization": f"Bearer {self.jwt_token}"
        }
        response = self.app.put('/ta/1', data=json.dumps(data), headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
    def test_delete_ta(self):
        headers = {
            "Authorization": f"Bearer {self.jwt_token}"
        }
        response = self.app.delete('/ta/1', headers=headers)
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()

