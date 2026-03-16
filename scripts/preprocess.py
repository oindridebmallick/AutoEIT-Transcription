import librosa
import noisereduce as nr
import soundfile as sf

def clean_audio(input_file, output_file):

    audio, sr = librosa.load(input_file, sr=16000)

    reduced_noise = nr.reduce_noise(y=audio, sr=sr)

    sf.write(output_file, reduced_noise, sr)

    return output_file