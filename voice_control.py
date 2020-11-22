import speech_recognition as sr
import pyaudio as py


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak")
        audio = r.listen(source)
        print("listening")
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception found:" + str(e))

    return said


