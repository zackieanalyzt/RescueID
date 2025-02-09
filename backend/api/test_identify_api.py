import unittest
from flask import Flask
from backend.api.identify.identify_api import identify_api

class TestIdentifyAPI(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.register_blueprint(identify_api)
        self.client = self.app.test_client()

    def test_identify_user_success(self):
        # Mock request data
        mock_data = {
            "image_path": "test_image.jpg",
            "thai_id": "1234567890123"
        }

        # Send POST request to /identify
        response = self.client.post('/identify', json=mock_data)
        data = response.get_json()

        # Assert response status and content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")
        self.assertIn("face_result", data)
        self.assertIn("user_data", data)
        self.assertIn("health_records", data)
        self.assertIn("blockchain_result", data)

    def test_identify_user_invalid_image(self):
        # Mock request data with invalid image path
        mock_data = {
            "image_path": "invalid_image.jpg",
            "thai_id": "1234567890123"
        }

        # Send POST request to /identify
        response = self.client.post('/identify', json=mock_data)
        data = response.get_json()

        # Assert response status and error message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["status"], "error")
        self.assertIn("message", data)

    def test_identify_user_not_found(self):
        # Mock request data with non-existent ThaiID
        mock_data = {
            "image_path": "test_image.jpg",
            "thai_id": "9999999999999"
        }

        # Send POST request to /identify
        response = self.client.post('/identify', json=mock_data)
        data = response.get_json()

        # Assert response status and error message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["message"], "User not found in database")

if __name__ == '__main__':
    unittest.main()
