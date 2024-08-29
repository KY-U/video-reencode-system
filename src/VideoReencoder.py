import subprocess
from EncodeConfig.EncodeConfig import EncodeConfig
import ffmpeg
import time 

class VideoReencoder:
    def __init__(self, encode_config: EncodeConfig, num_threads: int = 3):
        self.encode_config = encode_config
        self.num_threads = num_threads

    def reencode(self, input_path: str, output_path: str):
        codec = self.encode_config.get_codec()
        bitrate = self.encode_config.get_bitrate()
        crf = self.encode_config.get_crf()
        speed = self.encode_config.get_speed()

        #montando o comando FFMPEG
        '''
        command = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', codec,
            '-b:v', bitrate, #bitrate variável
            '-crf', str(crf),
            '-preset', speed,
            '-threads', str(self.num_threads), #metade de cores da minha CPU local
            output_path
        ]
        subprocess.run(command, check=True)
        '''
        try:
            #configura o comando FFmpeg usando a biblioteca ffmpeg-python
            (
                ffmpeg
                .input(input_path)
                .output(
                    output_path,
                    vcodec=codec,
                    **{'b:v': bitrate},  #bit_rate
                    #**{'minrate': bitrate},
                    **{'maxrate': '300k'},
                    crf=crf,
                    speed=speed, #vp8 e vp9 é speed, av1 é preset
                    threads=self.num_threads,
                    #pix_fmt='yuv420p'  #formato de pixel para compatibilidade com navegadores
                )
                .run(overwrite_output=True)  #sobrescrever o arquivo de saída se ele já existir
            )
        except ffmpeg.Error as e:
            print(f"Error occurred: {e.stderr.decode()}")

    #wrapper para contar o tempo de execução
    def reencode_timer(self, video_input_path, video_output_path):
        start_time = time.time()
        self.reencode(video_input_path, video_output_path)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Tempo de execução: {duration:.2f} segundos")
        with open('output.txt', 'a') as file:
            file.write("Tempo de execução:" + str(duration) +  "\n")
        

        
        
        

