import os
from services.VP8EncodeConfig import VP8EncodeConfig
from services.VP9EncodeConfig import VP9EncodeConfig
from services.AV1EncodeConfig import AV1EncodeConfig

class EncodeConfigFactory:
    @staticmethod
    def create_encode_config():
        codec = os.getenv('CODEC', 'libaom-av1')
        mode = os.getenv('MODE', 'variable')
        bitrate = os.getenv('BITRATE', '100k')
        max_bitrate = os.getenv('MAX_BITRATE', '300k')
        crf = int(os.getenv('CRF', 63))
        speed = os.getenv('SPEED', '8')
        num_threads = int(os.getenv('NUM_THREADS', '3'))
        if codec == 'libvpx-vp8':
            return VP8EncodeConfig( mode, bitrate, max_bitrate, crf, speed, num_threads)
        elif codec == 'libvpx-vp9':
            return VP9EncodeConfig(mode, bitrate, max_bitrate, crf, speed, num_threads)
        #libaom-av1
        else:
            return AV1EncodeConfig(mode, bitrate, max_bitrate, crf, speed, num_threads)