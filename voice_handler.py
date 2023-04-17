import speech_recognition as sr
import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('voice', 'fr')
    return engine

def speak(text, voice, engine):
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()

def get_voice(engine):
    voices = engine.getProperty('voices')
    for voice in voices:
        if "fr" in voice.languages:
            return voice
    return voices[0]

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="fr-FR")
        except sr.RequestError:
            print("Je n'ai pas compris ce que vous avez dit")
        except sr.UnknownValueError:
            print("Reconnaissance vocale échouée")
    return said