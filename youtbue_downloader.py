from pytube import YouTube

class youtube_downloader:
    def __init__(self, url):
        self.url = url

    def create_yt_object(self):
        # Create youtube object
        try:
            self.yt = YouTube(self.url)
            print("Youtube video created successfully")
            return self.yt
        except Exception:
            raise Exception("Error creating youtube object")

#yt = YouTube(link)

    def download_video_audio(self, path, audio_file_name):
        # Download audio from youtube video
        try:
            print("Downloading video audio...")
            stream = self.yt.streams.filter(only_audio=True).first()
            stream.download(filename=audio_file_name, output_path=path)
            print(f"YouTube video audio downloaded successfully to {path}/{audio_file_name}")
        except Exception:
            raise Exception("Error downloading audio")