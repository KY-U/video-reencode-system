from EncodeConfig.EncodeConfig import EncodeConfig

class VP8EncodeConfig(EncodeConfig):
    def __init__(self, bitrate: str, crf: int, speed: str):
        super().__init__(codec="libvpx", bitrate=bitrate, crf=crf, speed=speed)