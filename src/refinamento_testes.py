from EncodeConfig.VP8EncodeConfig import VP8EncodeConfig
from EncodeConfig.VP9EncodeConfig import VP9EncodeConfig
from EncodeConfig.AV1EncodeConfig import AV1EncodeConfig
from VideoReencoder import VideoReencoder
import os

def reencoding_test(codec_config, input_file, output_file, num_threads=3):
    reencoder = VideoReencoder(codec_config, num_threads=num_threads)
    reencoder.reencode_timer(input_file, output_file)

codec_configs = {
    1: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=30, speed=8),
    2: AV1EncodeConfig(mode = "variable", bitrate="100k", max_bitrate="300k", crf=30, speed=8),
    3: AV1EncodeConfig(mode = "variable", bitrate="200k", max_bitrate="300k", crf=30, speed=8),
    4: AV1EncodeConfig(mode = "variable", bitrate="200k", max_bitrate="300k", crf=30, speed=8),
    5: AV1EncodeConfig(mode = "variable", bitrate="300k", max_bitrate="300k", crf=30, speed=8),
    6: AV1EncodeConfig(mode = "variable", bitrate="300k", max_bitrate="300k", crf=30, speed=8),
    7: AV1EncodeConfig(mode = "variable", bitrate="400k", max_bitrate="300k", crf=30, speed=8),
    8: AV1EncodeConfig(mode = "variable", bitrate="400k", max_bitrate="300k", crf=30, speed=8),
    9: AV1EncodeConfig(mode = "variable", bitrate="500k", max_bitrate="300k", crf=30, speed=8),
    10: AV1EncodeConfig(mode = "variable", bitrate="500k", max_bitrate="300k", crf=30, speed=8),
}

#caminhos das pastas
current_path = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(current_path, "..", "5_trimmed_videos")
output_path = os.path.join(current_path, "..", "5_refinamento_output")

#testes
video_input_path = os.path.join(input_path, "h265.mp4")

for i in range(1, 11):
    file_name = f"h265_av1_{i}.webm"
    video_output_path = os.path.join(output_path, file_name)
    reencoding_test(codec_configs[i], video_input_path, video_output_path)
