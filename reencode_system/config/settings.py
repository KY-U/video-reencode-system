from dotenv import load_dotenv
import os

class Settings:
    def __init__(self):
        load_dotenv()
        self.APP_PORT = os.getenv("APP_PORT", 5000)
        self.VIDEO_CODEC = os.getenv("VIDEO_CODEC", "libvpx")
        self.ENCODE_MODE = os.getenv("ENCODE_MODE", "variable")
        self.BITRATE = os.getenv("BITRATE", "100k")
        self.MAX_BITRATE = os.getenv("MAX_BITRATE", "300k")
        self.CRF = int(os.getenv("CRF", 30))
        self.SPEED = os.getenv("SPEED", "8")
        self.NUM_THREADS = int(os.getenv("NUM_THREADS", -1))