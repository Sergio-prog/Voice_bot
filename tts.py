import pyttsx3

default_rate = 210
default_volume = 0.25

engine = pyttsx3.init()
engine.setProperty('rate', default_rate)
engine.setProperty('volume', default_volume)


def talk(text: str, is_print: bool = False):
    engine.say(text)
    if is_print:
        print(text)

    engine.runAndWait()
    return None
