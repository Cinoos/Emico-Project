import pyttsx3

# TTS setup (ONCE ONLY — important)
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)

def speak(text):
    print("Gandroid:", text)
    engine.say(text)
    engine.runAndWait()