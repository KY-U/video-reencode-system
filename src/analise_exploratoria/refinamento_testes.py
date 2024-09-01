
import os
import sys

#adicionando o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EncodeConfig.VP8EncodeConfig import VP8EncodeConfig
from EncodeConfig.VP9EncodeConfig import VP9EncodeConfig
from EncodeConfig.AV1EncodeConfig import AV1EncodeConfig
from VideoReencoder import VideoReencoder

def reencoding_test(codec_config, input_file, output_file, num_threads=3):
    reencoder = VideoReencoder(codec_config, num_threads=num_threads)
    reencoder.reencode_timer(input_file, output_file)

codec_configs = {
    1: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=0),
    2: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=1),
    3: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=2),
    4: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=3),
    5: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=4),
    6: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=5),
    7: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=6),
    8: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=7),
    9: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=63, speed=8)
}

#caminhos das pastas
current_path = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(current_path, "..", "..", "5_trimmed_videos")
output_path = os.path.join(current_path, "..", "..", "5_refinamento_output")

#testes
video_input_path = os.path.join(input_path, "h265.mp4")

##for i in range(1, 11):
for i in range(9, 0, -1):
    file_name = f"h265_av1_{i}.webm"
    video_output_path = os.path.join(output_path, file_name)
    reencoding_test(codec_configs[i], video_input_path, video_output_path)
