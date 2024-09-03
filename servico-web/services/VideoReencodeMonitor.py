from services.VideoReencoder import VideoReencoder
import time
import os

class VideoReencodeMonitor:
    def __init__(self, reencoder: VideoReencoder):
        self.reencoder = reencoder
    
    def reencode_with_monitoring(self, input_path: str, output_path: str):
        #título do vídeo
        words = output_path.split("\\")
        video = words[-1]

        #contando o tempo de reencode
        start_time = time.time()
        self.reencoder.reencode(input_path, output_path)
        end_time = time.time()
        duration = end_time - start_time

        #calculando tamanho do arquivo comprimido
        file_size = os.path.getsize(output_path) #bytes
        file_size_mb = file_size / (1024 * 1024) # mb

        #escrevendo no arquivo de log
        with open('output.txt', 'a') as file:
            file.write(f"Tempo de reencode de {video}: {duration:.0f} segundos, Tamanho: {file_size_mb} Mb\n")