import whisper
import sys
import os

def transcribe_audio(audio_path):
    # Check if file exists
    if not os.path.exists(audio_path):
        print(f"Error: File '{audio_path}' does not exist.")
        return
    
    try:
        # Load the model (you can choose different sizes: tiny, base, small, medium, large)
        print("Loading Whisper model...")
        model = whisper.load_model("small")
        
        print("Transcribing and translating audio...")
        # Transcribe the audio with translation to English
        result = model.transcribe(audio_path, task="translate")
        
        # Get original transcription
        original_result = model.transcribe(audio_path)
        
        print("\nOriginal Transcription:")
        print("---------------------")
        print(original_result["text"])
        
        print("\nEnglish Translation:")
        print("------------------")
        print(result["text"])
        
        print("\nDetected Language:", original_result["language"])
        
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python transcriber.py <path_to_audio_file>")
        sys.exit(1)
        
    audio_path = sys.argv[1]
    transcribe_audio(audio_path)

if __name__ == "__main__":
    main() 