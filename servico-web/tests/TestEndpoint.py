import unittest
import sys
import os
#adicionando o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestReencodeEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_reencode_invalid_data(self):
        client = app.test_client()

        #dados de teste inválidos
        data = {
            'input_path': '',  
            'output_path': 'output.mp4',
        }

        # Chamando o endpoint
        response = client.post('/reencode', json=data)

        #verificando o status de resposta e mensagem de erro
        self.assertEqual(response.status_code, 400) #bad request


if __name__ == '__main__':
    unittest.main()