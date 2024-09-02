import unittest
import sys
import os
#adicionando o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch
from services.EncodeConfigFactory import EncodeConfigFactory

class TestEncodeConfigFactory(unittest.TestCase):   
    @patch('config.settings.os.getenv')
    def test_default_encode_config(self, mock_getenv):
        #mock_getenv.side_effect = lambda key, default=None: default
        config = EncodeConfigFactory.create_encode_config()
        
        self.assertEqual(config._codec, "libaom-av1")
        self.assertEqual(config._mode, "variable")
        self.assertEqual(config._bitrate, "100k")
        self.assertEqual(config._max_bitrate, "-1")
        self.assertEqual(config._crf, 63)
        self.assertEqual(config._speed, "8")
        self.assertEqual(config._num_threads, -1)

if __name__ == '__main__':
    unittest.main()