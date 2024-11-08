from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytube.exceptions import VideoUnavailable
from files_utils import delete_files
from audio_utils import mp4_to_wav, audioToText
from openai_utils import summarizer


# Prompts The User To Enter A Video To Be Summarized

while True:
    url = input("Please input a youtube video to summarize: ")

    if "youtube.com/" in url:
        try:
            print("Downloading...")
            yt = YouTube(url, on_progress_callback = on_progress)
            ys = yt.streams.get_highest_resolution()
            ys.download("./VideoAudio")
            print("Video Downloaded!")
            path = f"./VideoAudio/{ yt.title }.mp4"
            wav_file = mp4_to_wav(path)
            text = audioToText(wav_file)
            summarizer(text)
            delete_files(wav_file, path)

        except VideoUnavailable:
            print("This video is unavailable for some reason! Please check link and try again!")
            break
    else:
        print("Invalid input!")
        continue
            


