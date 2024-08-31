from abc import ABC, abstractmethod

class EncodeConfig(ABC):
    def __init__(self, codec: str, mode: str="variable", bitrate: str="100k", max_bitrate: str="300k", crf: int=30, speed: str=8, ):
        self._codec = codec
        self._mode = mode
        self._bitrate = bitrate
        self._max_bitrate = max_bitrate
        self._crf = crf
        self._speed = speed

    def get_codec(self) -> str:
        return self._codec
    
    def get_mode(self) -> str:
        return self._mode
    
    def get_bitrate(self) -> str:
        return self._bitrate
    
    def get_max_bitrate(self) -> str:
        return self._max_bitrate
    
    def get_crf(self) -> int:
        return self._crf
    
    def get_speed(self) -> str:
        return self._speed