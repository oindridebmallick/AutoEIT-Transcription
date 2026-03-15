import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_file):

    result = model.transcribe(audio_file, language="es")

    return result["text"]
def transcribe_audio(audio_file):

    result = model.transcribe(audio_file, language="es")

    text = result["text"]
    confidence = result["segments"][0]["avg_logprob"]

    return text, confidence