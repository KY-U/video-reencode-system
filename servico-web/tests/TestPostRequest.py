import requests
import unittest

#
class   TestPostRequest(unittest.TestCase):
    #testa uma requisição de reencode de vídeo com um vídeo de exemplo
    def test_post_request(self):
        url = 'http://127.0.0.1:5000/reencode'

        data = {
            "video_source": "gs://psel_video_samples/h265.mp4"
        }

        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()