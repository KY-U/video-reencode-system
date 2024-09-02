import cv2
import numpy as np
import os
import sys

#adicionando o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def calculate_psnr(original_frame, compressed_frame):
    original = np.float32(original_frame)
    compressed = np.float32(compressed_frame)
    
    mse = np.mean((original - compressed) ** 2)
    
    if mse == 0:
        return float('inf')
    
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def calculate_video_psnr(original_video_path, compressed_video_path):
    original_cap = cv2.VideoCapture(original_video_path)
    compressed_cap = cv2.VideoCapture(compressed_video_path)
    
    psnr_values = []
    
    while True:
        ret1, original_frame = original_cap.read()
        ret2, compressed_frame = compressed_cap.read()
        
        if not ret1 or not ret2:
            break
        
        if original_frame.shape != compressed_frame.shape:
            raise ValueError("Dimensões de frames diferentes")
        
        psnr = calculate_psnr(original_frame, compressed_frame)
        psnr_values.append(psnr)
    
    original_cap.release()
    compressed_cap.release()
    
    if psnr_values:
        average_psnr = np.mean(psnr_values)
        with open('psnr_output.txt', 'a') as file:
            file.write("PSNR:" + str(average_psnr) +  "\n")
        return average_psnr
    else:
        return None

#caminhos das pastas
current_path = os.path.dirname(os.path.abspath(__file__))

#input_path = os.path.join(current_path, "..", "videos")
#output_path = os.path.join(current_path, "..", "output")

input_path = os.path.join(current_path, "..", "..", "5_trimmed_videos")
output_path = os.path.join(current_path, "..", "..", "5_refinamento_output")

video_input_path = os.path.join(input_path, "h265.mp4")

for i in range(1, 11):
    file_name = f"h265_av1_{i}.webm"
    video_output_path = os.path.join(output_path, file_name)
    if os.path.exists(video_output_path):
        average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
        print(f"Média PSNR {i}: {average_psnr_value} dB")
        with open('psnr_output.txt', 'a') as file:
            file.write("Média PSNR " + str(i) + ":" + str(average_psnr_value) +  "\n")
    else:
        print(f"Arquivo {file_name} não encontrado")
        


'''
input_path = os.path.join(current_path, "..", "5_trimmed_videos")
output_path = os.path.join(current_path, "..", "5_refinamento_output")
video_input_path = os.path.join(input_path, "h265.mp4")
video_output_path = os.path.join(output_path, "h265_av1_1.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
'''

'''
#TESTES VP8
#H264 - VP8
video_input_path = os.path.join(input_path, "h264.mp4")
video_output_path = os.path.join(output_path, "h264_vp8.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

#H264+ - VP8
video_input_path = os.path.join(input_path, "h264+.mp4")
video_output_path = os.path.join(output_path, "h264+_vp8.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

#H265 - VP8
video_input_path = os.path.join(input_path, "h265.mp4")
video_output_path = os.path.join(output_path, "h265_vp8.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

#TESTES VP9
#H264 - VP9
video_input_path = os.path.join(input_path, "h264.mp4")
video_output_path = os.path.join(output_path, "h264_vp9.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

#H264+ - VP9
video_input_path = os.path.join(input_path, "h264+.mp4")
video_output_path = os.path.join(output_path, "h264+_vp9.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

#H265 - VP9
video_input_path = os.path.join(input_path, "h265.mp4")
video_output_path = os.path.join(output_path, "h265_vp9.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

#TESTES AV1
#H264 - AV1
video_input_path = os.path.join(input_path, "h264.mp4")
video_output_path = os.path.join(output_path, "h264_av1.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

#H264+ - AV1
video_input_path = os.path.join(input_path, "h264+.mp4")
video_output_path = os.path.join(output_path, "h264+_av1.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

#H265 - AV1
video_input_path = os.path.join(input_path, "h265.mp4")
video_output_path = os.path.join(output_path, "h265_av1.webm")
average_psnr_value = calculate_video_psnr(video_input_path, video_output_path)
print(f"Média PSNR: {average_psnr_value} dB")

'''
