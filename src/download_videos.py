import os
from google.cloud import storage

def main():
    client = storage.Client.create_anonymous_client()
    bucket = client.bucket(bucket_name='psel_video_samples')

    base_dir = os.path.dirname(os.path.abspath(__file__))

    videos_dir = os.path.join(base_dir, '..', 'videos')
    print(f"videos_dir: {videos_dir}")

    #Vídeos teste
    blob = bucket.blob('h264.mp4')
    blob.download_to_filename(os.path.join(videos_dir, 'h264.mp4'))

    blob = bucket.blob('h264+.mp4') 
    blob.download_to_filename(os.path.join(videos_dir, 'h264+.mp4'))

    blob = bucket.blob('h265.mp4') 
    blob.download_to_filename(os.path.join(videos_dir, 'h265.mp4'))

if __name__ == "__main__":
    main()