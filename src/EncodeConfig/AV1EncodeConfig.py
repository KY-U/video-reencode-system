from EncodeConfig.EncodeConfig import EncodeConfig

class AV1EncodeConfig(EncodeConfig):
    def __init__(self, bitrate: str, crf: int, speed: str):
        super().__init__(codec="libaom-av1", bitrate=bitrate, crf=crf, speed=speed)