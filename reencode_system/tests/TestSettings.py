import unittest
import sys
import os
#adicionando o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import Settings
from unittest.mock import patch

class TestSettings(unittest.TestCase):
    #testando as configurações padrões
    #de variáveis de ambiente
    @patch('config.settings.os.getenv')
    def test_default_values(self, mock_getenv):
        #configura o mock para retornar None para todas as chamadas de getenv
        mock_getenv.return_value = None
        
        #instancia a classe Settings
        settings = Settings()
        #verifica se os valores padrão estão corretos
        self.assertEqual(settings.APP_PORT, 5000)
        self.assertEqual(settings.VIDEO_CODEC, 'libaom-av1')
        self.assertEqual(settings.ENCODE_MODE, 'variable')
        self.assertEqual(settings.BITRATE, '100k')
        self.assertEqual(settings.MAX_BITRATE, '-1')
        self.assertEqual(settings.CRF, 63)
        self.assertEqual(settings.SPEED, '8')
        self.assertEqual(settings.NUM_THREADS, -1)

if __name__ == '__main__':
    unittest.main()