from flask import jsonify
from services.VideoReencoder import VideoReencoder
from services.VideoReencodeMonitor import VideoReencodeMonitor
from services.EncodeConfigFactory import EncodeConfigFactory
from services.VideoManager import VideoManager
import os

class VideoReencoderController:
    def __init__(self, video_source: str):
        self.video_source = video_source

    def reencode_video(self):
        #baixar vídeo
        video_manager = VideoManager(self.video_source)
        video_manager.download_video()

        #caminhos
        video_path = video_manager.get_video_path()
        output_path = video_manager.get_output_video_path()

        #instanciando as configurações de encoding e o encoder
        encode_config = EncodeConfigFactory.create_encode_config()
        reencoder = VideoReencoder(encode_config) 

        #monitorando o reencode
        monitor = VideoReencodeMonitor(reencoder)
        monitor.reencode_with_monitoring(video_path, output_path)

        return jsonify({"message": "Reencode completo!", "output_path": output_path})
    