from services.VideoReencoder import VideoReencoder
from services.VideoReencodeMonitor import VideoReencodeMonitor
from services.EncodeConfigFactory import EncodeConfigFactory
from services.VideoManager import VideoManager
from services.VideoReencoderController import VideoReencoderController
from config.settings  import Settings

from flask import Flask, request, jsonify
from dotenv import load_dotenv

#carregar as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

@app.route('/reencode', methods=['POST'])
def reencode_video():
    #recebe o vídeo a ser reencoded
    data = request.get_json()
    video_source = data.get('video_source')
    if not video_source:
        return jsonify({"error": "No video source provided"}), 400
    
    #controlador para reencode de vídeo
    reencode_controller = VideoReencoderController(video_source)
    response = reencode_controller.reencode_video()
    return response
    

if __name__ == '__main__':
    settings = Settings()  #carrega as configurações do .env, se não houver, carrega as configurações padrão
    app.run(host='0.0.0.0', port=settings.APP_PORT, threaded=True) #threaded=True permite múltiplas requisições simultâneas