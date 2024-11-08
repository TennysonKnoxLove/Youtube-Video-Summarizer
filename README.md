# YouTube Video Summarizer

A Python project that allows users to input a YouTube video URL, download the video, convert it to audio, transcribe the audio, and summarize the content using OpenAI's GPT model.

## Features

- Download YouTube videos using `pytube` library.
- Convert video to audio (`.wav`) using `moviepy`.
- Transcribe audio using Google Cloud Speech-to-Text.
- Summarize the transcribed text using OpenAI's GPT model.
- Clean up by deleting intermediate files after summarization.

## Requirements

To run this project, you will need Python 3.x and several Python libraries. Please make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- `pytube` for downloading YouTube videos.
- `moviepy` for converting video to audio.
- `speech_recognition` for transcribing audio.
- `openai` for summarizing the transcribed text.
- `pytubefix` for a more stable YouTube downloader.
- `concurrent.futures` (part of Python standard library) for parallel processing of audio chunks.

### Install dependencies using pip:

```bash
pip install pytube moviepy openai speechrecognition pytubefix
