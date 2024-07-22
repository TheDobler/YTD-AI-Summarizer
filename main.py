# from pytube import YouTube
import os
import sys

from youtbue_downloader import *
from whisper_ai import *

_audio_file_name = "audio_english.mp3"
_output_file_name = "output.txt"
_folder_name = "folderName.txt"

# Create a function that will remove space in the title of the video
def replace_space(string):
    return ''.join(c for c in string if c not in " ")

def create_folder(path):
    # Create a folder for the videos if it doesn't exist already with yt.title as folder name
    if not os.path.exists(path):
        os.mkdir(path)

# Get the YouTube video link from the user
link = input("Enter the YouTube video link: ")
# Create a instance of the youtube_downloader class
youtube = youtube_downloader(link)
try:
   # Create a YouTube object from the link
   yt = youtube.create_yt_object()
except Exception as error:
   print(error)
   sys.exit()

print("Video title: " + yt.title)
Title = replace_space(yt.title)
path = "./Downloads/"+Title
audio_path = path + "/" + _audio_file_name

create_folder(path)

try:
   youtube.download_video_audio(path, _audio_file_name)
except Exception as error:
    print(error)
    sys.exit()

model_type = input("What model do you want? (tiny, base (default), small, medium, large) ")
print(model_type + " is registered")
try:
   whisper_model = whisper_ai(model_type)
   model = whisper_model.load_whisper_model()
   result = whisper_model.transcribe_audio(audio_path)
except Exception as e:
    print(e)
    sys.exit()

# output_path = path+"/" +_output_file_name
text = open(path+"/" +_output_file_name, "w")
print("Writing to file...")
text.write(result["text"])
text.close()

# folder_name = "folderName.txt"
folder_text = open(f"./{_folder_name}","w")
folder_text.write(Title)
folder_text.close()

print("Done!")