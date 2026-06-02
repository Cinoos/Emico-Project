import sounddevice as sd
from scipy.io.wavfile import write
import os

SAMPLE_RATE = 16000
CHANNELS = 1

def record_audio(duration):
    base_dir = os.path.dirname(__file__)
    audio_path = os.path.join(base_dir, "audio", "input.wav")

    print("Speak")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )

    sd.wait()

    print("Done")

    write(audio_path, SAMPLE_RATE, audio)
    return audio_path