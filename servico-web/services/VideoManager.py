from google.cloud import storage
import os
class VideoManager:
    def __init__(self, url: str):
        #remover prefixo
        url = url.replace("gs://", "")
        #separar bucket e nome do vídeo
        self.bucket_name, self.video_name = url.split("/")

        #diretório de vídeos baixados
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.videos_dir = os.path.join(base_dir, '..','downloads')
        #caminho completo do vídeo
        self.video_path = os.path.join(self.videos_dir, self.video_name)

        #diretório de vídeos processados
        self.processed_videos_dir = os.path.join(base_dir, '..','processed_videos')

        #cria os diretórios se não existirem
        if not os.path.exists(self.videos_dir):
            os.makedirs(self.videos_dir)

        if not os.path.exists(self.processed_videos_dir):
            os.makedirs(self.processed_videos_dir)

    def get_processed_videos_dir(self):
        return self.processed_videos_dir

    def get_bucket_name(self):
        return self.bucket_name
    
    def get_video_name(self):
        return self.video_name
    
    def get_videos_dir(self):
        return self.videos_dir
    
    def get_video_path(self):
        return self.video_path
    
    def get_output_video_path(self):
        video_title = self.video_name.split(".")[0]
        #todos os codecs finais suportam o formato webm
        return os.path.join(self.processed_videos_dir, f"{video_title}.webm")
    
    #baixa o vídeo do bucket
    def download_video(self):
        client = storage.Client.create_anonymous_client()
        bucket = client.bucket(self.bucket_name)

        blob = bucket.blob(self.video_name)
        blob.download_to_filename(self.video_path)
    
    
    