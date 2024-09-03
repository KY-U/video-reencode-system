
#NAO ESTA FUNCIONANDO, NAO ESTA SENDO POSSIVEL IMPORTAR O VideoManager

import unittest
import sys
import os
#adicionando o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.VideoManager import VideoManager
from unittest.mock import patch


class TestVideoManager(unittest.TestCase):
    #testa caminho do vídeo gerado
    #dando problema com o patch
    @patch('video_manager.VideoManager.download_video')
    def test_video_path_generation(self, mock_download_video):
        mock_download_video.return_value = None  

        #instancia o VideoManager
        video_source = "gs://example.com/video.mp4"
        manager = VideoManager(video_source)
        manager.download_video()

        #verifica se o caminho do vídeo baixado é gerado corretamente
        #C:\Users\arcoc\github\video-reencode-system\reencode_system\downloads\video.mp4
        expected_path = f"downloads/video.mp4"
        print(manager.get_video_path())
        self.assertEqual(manager.get_video_path(), expected_path)

    
if __name__ == '__main__':
    unittest.main()