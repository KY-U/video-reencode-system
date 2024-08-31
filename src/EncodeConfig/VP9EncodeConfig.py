from EncodeConfig.EncodeConfig import EncodeConfig

class VP9EncodeConfig(EncodeConfig):
    def __init__(self, mode: str, bitrate: str, max_bitrate: str, crf: int, speed: str):
        super().__init__(codec="libvpx-vp9",mode=mode, bitrate=bitrate, max_bitrate=max_bitrate, crf=crf, speed=speed)