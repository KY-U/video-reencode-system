from abc import ABC, abstractmethod

class EncodeConfig(ABC):
    def __init__(self, codec: str, bitrate: str, crf: int, speed: str):
        self._codec = codec
        self._bitrate = bitrate
        self._crf = crf
        self._speed = speed

    def get_codec(self) -> str:
        return self._codec
    
    def get_bitrate(self) -> str:
        return self._bitrate
    
    def get_crf(self) -> int:
        return self._crf
    
    def get_speed(self) -> str:
        return self._speed