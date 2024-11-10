from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytube.exceptions import VideoUnavailable
from files_utils import delete_files
from audio_utils import mp4_to_wav, audioToText
from openai_utils import summarizer

#Prompts The User To Input A Video To Be Summarized.
while True:
    url = input("Please input a youtube video to summarize: ")

    if "youtube.com/" in url:
        try:
            print("Downloading...")
            yt = YouTube(url, on_progress_callback=on_progress)
            ys = yt.streams.get_highest_resolution()
            safe_title = "videotosummarize.mp4"
            ys.download("./VideoAudio", safe_title)
            print("Video Downloaded!")
            print(f"Saved as: {safe_title}")
            path = f"./VideoAudio/{safe_title}"
            wav_file = mp4_to_wav(path)
            text = audioToText(wav_file)
            summarizer(text)
            delete_files(wav_file, path)
        except VideoUnavailable:
            print("This video is unavailable for some reason! Please check the link and try again.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            delete_files(path)
            break
    else:
        print("Invalid input! Please provide a valid YouTube URL.")
        continue
