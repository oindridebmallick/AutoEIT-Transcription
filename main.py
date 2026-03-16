import os
from scripts.preprocess import clean_audio
from scripts.transcribe import transcribe_audio
from scripts.clean_text import clean_transcript
from scripts.evaluate import evaluate

audio_file = "audio/sample.mp3"
clean_file = "audio/clean.wav" # Using .wav to support standard soundfile writes

reference_text = "el niño está jugando en el parque"

if not os.path.exists(audio_file):
    print(f"Error: Could not find audio input file at '{audio_file}'.")
    print("Please make sure the file exists.")
    exit(1)

print("Step 1: Preprocessing audio...")
try:
    clean_audio(audio_file, clean_file)
except Exception as e:
    print(f"Failed during preprocessing: {e}")
    exit(1)

print("Step 2: Transcribing audio...")
try:
    text, confidence = transcribe_audio(clean_file)
except Exception as e:
    print(f"Failed during transcription: {e}")
    exit(1)

print("Step 3: Cleaning transcript...")
try:
    transcript = clean_transcript(text)
except Exception as e:
    print(f"Failed during text cleaning: {e}")
    exit(1)

print(f"Transcription: {transcript}")
print(f"Confidence (avg logprob): {confidence:.2f}")

print("Step 4: Evaluating...")
try:
    accuracy = evaluate(reference_text, transcript)
    print(f"Accuracy: {accuracy:.2f}%")
except Exception as e:
    print(f"Failed during evaluation: {e}")
    exit(1)
