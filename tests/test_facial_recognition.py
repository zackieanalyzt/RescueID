import unittest
from backend.api.facial_recognition import recognize_face

class TestFacialRecognition(unittest.TestCase):
    def test_recognize_face(self):
        result = recognize_face("test_image.jpg")
        self.assertEqual(result["status"], "success")

if __name__ == '__main__':
    unittest.main()
