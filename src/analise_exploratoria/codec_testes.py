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
    "vp8": VP8EncodeConfig(bitrate="100k", crf=30, speed=16),
    "vp9": VP9EncodeConfig(bitrate="100k", crf=30, speed=8),
    "av1": AV1EncodeConfig(bitrate="100k", crf=30, speed=8)  
}

#caminhos das pastas
current_path = os.path.dirname(os.path.abspath(__file__))


#input_path = os.path.join(current_path, "..", "videos")
#output_path = os.path.join(current_path, "..", "output")


input_path = os.path.join(current_path, "..", "..","5_trimmed_videos")
output_path = os.path.join(current_path, "..", "..","5_trimmed_output")

#TESTES VP8
#H264 - VP8
video_input_path = os.path.join(input_path, "h264.mp4")
video_output_path = os.path.join(output_path, "h264_vp8.webm")
reencoding_test(codec_configs["vp8"], video_input_path, video_output_path)

#H264+ - VP8
video_input_path = os.path.join(input_path, "h264+.mp4")
video_output_path = os.path.join(output_path, "h264+_vp8.webm")
reencoding_test(codec_configs["vp8"], video_input_path, video_output_path)

#H265 - VP8
video_input_path = os.path.join(input_path, "h265.mp4")
video_output_path = os.path.join(output_path, "h265_vp8.webm")
reencoding_test(codec_configs["vp8"], video_input_path, video_output_path)

#TESTES VP9
#H264 - VP9
video_input_path = os.path.join(input_path, "h264.mp4")
video_output_path = os.path.join(output_path, "h264_vp9.webm")
reencoding_test(codec_configs["vp9"], video_input_path, video_output_path)

#H264+ - VP9
video_input_path = os.path.join(input_path, "h264+.mp4")
video_output_path = os.path.join(output_path, "h264+_vp9.webm")
reencoding_test(codec_configs["vp9"], video_input_path, video_output_path)

#H265 - VP9
video_input_path = os.path.join(input_path, "h265.mp4")
video_output_path = os.path.join(output_path, "h2654_vp9.webm")
reencoding_test(codec_configs["vp9"], video_input_path, video_output_path)

#TESTES AV1
#H264 - AV1
video_input_path = os.path.join(input_path, "h264.mp4")
video_output_path = os.path.join(output_path, "h264_av1.webm")
reencoding_test(codec_configs["av1"], video_input_path, video_output_path)

#H264+ - AV1
video_input_path = os.path.join(input_path, "h264+.mp4")
video_output_path = os.path.join(output_path, "h264+_av1.webm")
reencoding_test(codec_configs["av1"], video_input_path, video_output_path)

#H265 - AV1
video_input_path = os.path.join(input_path, "h265.mp4")
video_output_path = os.path.join(output_path, "h265_av1.webm")
reencoding_test(codec_configs["av1"], video_input_path, video_output_path)