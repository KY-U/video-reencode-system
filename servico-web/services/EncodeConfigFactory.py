import os
from services.VP8EncodeConfig import VP8EncodeConfig
from services.VP9EncodeConfig import VP9EncodeConfig
from services.AV1EncodeConfig import AV1EncodeConfig

class EncodeConfigFactory:
    @staticmethod
    def create_encode_config():
        codec = os.environ.get('CODEC', 'libaom-av1')
        mode = os.environ.get('MODE', 'variable')
        bitrate = os.environ.get('BITRATE', '100k')
        max_bitrate = os.environ.get('MAX_BITRATE', '-1')
        crf = int(os.environ.get('CRF', 63))
        speed = os.environ.get('SPEED', '8')
        num_threads = int(os.environ.get('NUM_THREADS', '-1'))
        if codec == 'libvpx-vp8':
            return VP8EncodeConfig( mode, bitrate, max_bitrate, crf, speed, num_threads)
        elif codec == 'libvpx-vp9':
            return VP9EncodeConfig(mode, bitrate, max_bitrate, crf, speed, num_threads)
        #libaom-av1
        else:
            return AV1EncodeConfig(mode, bitrate, max_bitrate, crf, speed, num_threads)