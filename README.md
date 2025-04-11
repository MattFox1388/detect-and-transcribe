# Audio Transcription and Translation Tool

A Docker-based tool that transcribes audio files and translates them to English using OpenAI's Whisper model.

## Prerequisites

- Docker installed on your system
  - [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop)
  - [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
  - Linux: `sudo apt-get install docker.io`

## Setup

1. Clone or create project directory with these files:
```bash
docker build -t speech-transcriber .
```

## Usage

Run the transcriber with your audio file:
```bash
docker run -v $(pwd):/app speech-transcriber python transcriber.py /app/your_audio_file
```

Example:
```bash
docker run -v $(pwd):/app speech-transcriber python transcriber.py /app/meeting.mp3
```

## Features

- Supports multiple audio formats (MP3, WAV, etc.)
- Detects source language automatically
- Provides original transcription and English translation
- Works offline (no API keys needed)
- Uses Python 3.7.9 in a containerized environment

## Model Options

You can modify the model size in transcriber.py:
- "tiny": Fastest, least accurate
- "base": Good balance (default)
- "small": More accurate but slower
- "medium": Even more accurate
- "large": Most accurate, requires more resources

## Troubleshooting

1. If Docker isn't found:
   ```bash
   command not found: docker
   ```
   → Install Docker using the prerequisites links above

2. If audio file isn't found:
   - Make sure your audio file is in the same directory as your Dockerfile
   - Check the path in your docker run command

3. If build fails:
   - Check internet connection
   - Ensure Dockerfile and requirements.txt are in your directory