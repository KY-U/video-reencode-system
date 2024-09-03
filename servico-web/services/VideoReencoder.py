from services.EncodeConfig import EncodeConfig
import ffmpeg
#import time 
#import os
class VideoReencoder:
    def __init__(self, encode_config: EncodeConfig):
        self.encode_config = encode_config
    
    def reencode(self, input_path: str, output_path: str):
        codec = self.encode_config.get_codec()
        mode = self.encode_config.get_mode()
        bitrate = self.encode_config.get_bitrate()
        max_rate = self.encode_config.get_max_bitrate()
        crf = self.encode_config.get_crf()
        speed = self.encode_config.get_speed()
        num_threads = self.encode_config.get_num_threads()

        #dicionário de argumentos
        output_args = {
        'vcodec': codec,
        'crf': crf,
        }

        #caso o número de threads esteja definido
        if num_threads != -1:
            output_args['threads'] = num_threads

        #configuração 'Deadline' específica de codec
        if codec == "libaom-av1":
            output_args['cpu-used'] = speed  #av1
        else:
            output_args['speed'] = speed  #vp8 e vp9

        #para modos variable e fix seta bitrate
        if mode != "unset":
            output_args['b:v'] = bitrate
        #bitrate variável
        if mode == "variable" and max_rate != "-1":
            #bitrate max opcional
            output_args['maxrate'] = max_rate
        #bitrate fixo        
        elif mode == "fix":
            output_args['maxrate'] = bitrate
            output_args['bufsize'] = bitrate
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
            print(f"Erro Ocorreu: {e.stderr.decode()}")