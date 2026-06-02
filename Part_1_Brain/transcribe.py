import whisper

model = whisper.load_model("base")

def transcribe_audio(filename="input.wav"):
    result = model.transcribe(filename)

    text = result["text"]

    print("Transcription:")
    print(text)

    return text


if __name__ == "__main__":
    transcribe_audio()