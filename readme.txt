# Transcriber

1. docker build -t speech-transcriber .
2. docker run -v $(pwd):/app speech-transcriber python transcriber.py /app/your_audio.wav