from services.EncodeConfig import EncodeConfig

class VP8EncodeConfig(EncodeConfig):
    def __init__(self, mode: str, bitrate: str, max_bitrate: str, crf: int, speed: str, num_threads: int):
        super().__init__(codec="libvpx",mode=mode, bitrate=bitrate, max_bitrate=max_bitrate,crf=crf, speed=speed, num_threads=num_threads)