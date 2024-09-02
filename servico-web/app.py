from services.VideoReencoder import VideoReencoder
from services.VideoReencodeMonitor import VideoReencodeMonitor
from services.EncodeConfigFactory import EncodeConfigFactory
from services.VideoManager import VideoManager
from config.settings  import Settings

from flask import Flask, request, jsonify
from dotenv import load_dotenv

#carregar as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

@app.route('/reencode', methods=['POST'])
def reencode_video():
    data = request.get_json()
    video_source = data.get('video_source')
    if not video_source:
        return jsonify({"error": "No video source provided"}), 400

    #Baixar vídeo
    video_manager = VideoManager(video_source)
    video_manager.download_video()

    #caminhos
    video_path = video_manager.get_video_path()
    output_path = video_manager.get_output_video_path()

    #Instanciando as configurações de encoding e o encoder
    encode_config = EncodeConfigFactory.create_encode_config()
    reencoder = VideoReencoder(encode_config) 

    # Monitorando o reencode
    monitor = VideoReencodeMonitor(reencoder)
    monitor.reencode_with_monitoring(video_path, output_path)

    return jsonify({"message": "Reencode completo!", "output_path": output_path})

if __name__ == '__main__':
    settings = Settings()  #carrega as configurações do .env
    app.run(host='0.0.0.0', port=settings.APP_PORT, threaded=True)