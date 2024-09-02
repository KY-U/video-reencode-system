from dotenv import load_dotenv
import os

class Settings:
    def __init__(self):
        load_dotenv()
        #por algum motivo, os.getenv sempre retorna None
        self.APP_PORT = int(os.environ.get("APP_PORT", 5000))
        self.VIDEO_CODEC = os.environ.get("VIDEO_CODEC", "libaom-av1")
        self.ENCODE_MODE = os.environ.get("ENCODE_MODE", "variable")
        self.BITRATE = os.environ.get("BITRATE", "100k")
        self.MAX_BITRATE = os.environ.get("MAX_BITRATE", "-1")
        self.CRF = int(os.environ.get("CRF", 63))
        self.SPEED = os.environ.get("SPEED", "8")
        self.NUM_THREADS = int(os.environ.get("NUM_THREADS", -1))