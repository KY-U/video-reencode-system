from EncodeConfig.EncodeConfig import EncodeConfig

class VP9EncodeConfig(EncodeConfig):
    def __init__(self, bitrate: str, crf: int, speed: str):
        super().__init__(codec="libvpx-vp9", bitrate=bitrate, crf=crf, speed=speed)