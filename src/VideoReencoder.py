import subprocess
from EncodeConfig.EncodeConfig import EncodeConfig
import ffmpeg
import time 
import os
class VideoReencoder:
    def __init__(self, encode_config: EncodeConfig, num_threads: int = 3):
        self.encode_config = encode_config
        self.num_threads = num_threads

    def reencode(self, input_path: str, output_path: str):
        codec = self.encode_config.get_codec()
        mode = self.encode_config.get_mode
        bitrate = self.encode_config.get_bitrate()
        max_rate = self.encode_config.get_max_bitrate()
        crf = self.encode_config.get_crf()
        speed = self.encode_config.get_speed()
        
        #dicionário de argumentos
        output_args = {
        'vcodec': codec,
        #'b:v': bitrate, 
        #'maxrate': '300k',
        'crf': crf,
        'threads': self.num_threads,
        }
        #configuração de codec
        if codec == "libaom-av1":
            output_args['cpu-used'] = speed  #av1
        else:
            output_args['speed'] = speed  #vp8 e vp9

        #configuração de bitrate
        if mode == "variable":
            output_args['b:v': bitrate,]
            output_args['maxrate': max_rate,]
        elif mode == "fix":
            output_args['b:v': bitrate,]
            output_args['maxrate': bitrate]
            output_args['buffsize': bitrate]
        #se for 'unset' nao seta bitrate
        
        #rodando comando ffmpeg
        try:
            #configura o comando FFmpeg usando a biblioteca ffmpeg-python
            (
                ffmpeg
                .input(input_path)
                .output(
                    output_path,
                    **output_args
                )
                .run(overwrite_output=True)  #sobrescrever o arquivo de saída se ele já existir
            )
        except ffmpeg.Error as e:
            print(f"Error occurred: {e.stderr.decode()}")

    #wrapper para contar o tempo de execução
    def reencode_timer(self, video_input_path, video_output_path):
        #split
        words = video_output_path.split("\\")
        video = words[-1]
        #contando o tempo de reencode
        start_time = time.time()
        self.reencode(video_input_path, video_output_path)
        end_time = time.time()
        duration = end_time - start_time

        #calculando tamanho do arquivo comprimido
        file_size = os.path.getsize(video_output_path) #bytes
        #file_size_kb = file_size / 1024 # kb
        file_size_mb = file_size / (1024 * 1024) # mb
        #print(f"Tempo de reencode de {video}: {duration:.2f} segundos")
        with open('output.txt', 'a') as file:
            file.write("Tempo de reencode de " + video + ": "+ str(duration) + " Tamanho: " + str(file_size_mb) + " Mb\n")
        

        
        
        

