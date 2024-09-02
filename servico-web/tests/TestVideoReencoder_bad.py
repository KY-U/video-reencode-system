#NAO ESTA FUNCIONANDO

import unittest
from unittest.mock import Mock, patch
import sys
import os
#adicionando o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.VideoReencoder import VideoReencoder
from services.EncodeConfig import EncodeConfig
import ffmpeg

class TestVideoReencoder(unittest.TestCase):
    @patch('ffmpeg.run')
    @patch('ffmpeg.output')
    @patch('ffmpeg.input')
    def test_reencode_process(self, mock_ffmpeg_input, mock_ffmpeg_output, mock_ffmpeg_run):
        # Mockando a configuração
        config = Mock(spec=EncodeConfig)
        config.get_codec.return_value = 'libaom-av1'
        config.get_mode.return_value = 'variable'
        config.get_bitrate.return_value = '100k'
        config.get_max_bitrate.return_value = '300k'
        config.get_crf.return_value = 63
        config.get_speed.return_value = '8'
        config.get_num_threads.return_value = 4


        reencoder = VideoReencoder(config)
        reencoder.reencode('input.mp4', 'output.mp4')


        output_args = {
            'vcodec': 'libaom-av1',
            'crf': 63,
            'threads': 4,
            'cpu-used': '8',
            'b:v': '100k',
            'maxrate': '300k'
        }
        print(output_args)


        mock_ffmpeg_input.assert_called_with('input.mp4')
        mock_ffmpeg_output.assert_called_with(
            'output.mp4',
            **output_args
        )
        mock_ffmpeg_run.assert_called_once_with(overwrite_output=True)



    def test_initialization(self):
        config = Mock(spec=EncodeConfig)
        reencoder = VideoReencoder(config)
        self.assertEqual(reencoder.encode_config, config)

if __name__ == '__main__':
    unittest.main()