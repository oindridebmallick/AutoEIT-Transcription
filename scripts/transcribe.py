import whisper
import librosa
import numpy as np

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    print(f"Transcribing {audio_file}...")
    
    # Load audio natively using librosa at 16kHz (whisper's expected sample rate)
    # This avoids whisper calling ffmpeg as a subprocess which errors out if ffmpeg is not installed
    audio_data, _ = librosa.load(audio_file, sr=16000)
    audio_data = audio_data.astype(np.float32)
    
    result = model.transcribe(audio_data, language="es")

    text = result.get("text", "")
    segments = result.get("segments", [])
    confidence = segments[0]["avg_logprob"] if segments else 0.0

    return text, confidence