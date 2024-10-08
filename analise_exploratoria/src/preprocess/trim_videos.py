import os
import ffmpeg
import sys

#adicionando o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def trim_video(video_input_path, video_output_path, start, end):
    (
	ffmpeg.input(video_input_path, ss=start, to=end)
	.output(video_output_path)
	.run()
    )

start = '00:00:00' 
end = '00:5:00' 

#caminhos das pastas
current_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_path, "..", "..", "videos")
output_path = os.path.join(current_path, "..", "..", "5_trimmed_videos")

if not os.path.exists(output_path):
	os.makedirs(output_path)

#cortando vídeos
video_input_path = os.path.join(input_path, "h264.mp4")
video_output_path = os.path.join(output_path, "h264.mp4")
trim_video(video_input_path, video_output_path, start, end)

video_input_path = os.path.join(input_path, "h264+.mp4")
video_output_path = os.path.join(output_path, "h264+.mp4")
trim_video(video_input_path, video_output_path, start, end)

video_input_path = os.path.join(input_path, "h265.mp4")
video_output_path = os.path.join(output_path, "h265.mp4")
trim_video(video_input_path, video_output_path, start, end)
