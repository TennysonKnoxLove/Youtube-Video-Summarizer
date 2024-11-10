import wave
import speech_recognition as sr
from concurrent.futures import ThreadPoolExecutor
import io
from moviepy.editor import VideoFileClip

def mp4_to_wav(mp4_file):
    wav_file = './VideoAudio/audiofile.wav'
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(wav_file)
    audio.close()
    video.close()
    print(f"Conversion complete! Saved MP3 as {wav_file}")
    return wav_file


def split_audio_in_memory(file_path, chunk_length=900000):
    chunks = []
    with wave.open(file_path, 'rb') as audio_file:
        sample_width = audio_file.getsampwidth()
        frame_rate = audio_file.getframerate()
        frame_count = audio_file.getnframes()
        
        for start in range(0, frame_count, chunk_length):
            end = min(start + chunk_length, frame_count)
            audio_file.setpos(start)
            frames = audio_file.readframes(end - start)
            
            audio_chunk = io.BytesIO()
            with wave.open(audio_chunk, 'wb') as chunk_file:
                chunk_file.setnchannels(1)
                chunk_file.setsampwidth(sample_width)
                chunk_file.setframerate(frame_rate)
                chunk_file.writeframes(frames)
            audio_chunk.seek(0)
            chunks.append(audio_chunk)
    return chunks

def transcribe_chunk(r, audio_chunk):
    try:
        with sr.AudioFile(audio_chunk) as source:
            audio_data = r.record(source)
            text = r.recognize_google_cloud(audio_data, credentials_json='INPUT GOOGLE CLOUD JSON API KEY')
            return text
    except Exception as e:
        print(f"Error transcribing chunk: {e}")
        return ""

def audioToText(wav_file):
    
    print("Reviewing Content...")
    print("\n")
    r = sr.Recognizer()
    chunks = split_audio_in_memory(wav_file)
    text = ""
    
    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda chunk: transcribe_chunk(r, chunk), chunks)
        
    for result in results:
        text += result + "\n"
    return text


