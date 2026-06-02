import pyttsx3

# TTS setup (ONCE ONLY — important)
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Gandroid:", text)
    engine.say(text)
    engine.runAndWait()