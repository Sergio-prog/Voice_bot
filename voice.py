import pyttsx3
import time
import speech_recognition as sr
from typing import Union
import os
import config
from config import commands_list
import commands

__ver__ = config.__ver__


def speech_to_text():
    with micro:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognize.adjust_for_ambient_noise(micro, duration=2)

        try:
            print("Listening...")
            audio = recognize.listen(micro, 5, 5)

        except sr.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        try:
            recognized_data = recognize.recognize_google(audio,
                                                         language=config.recognition_language).lower()

        except sr.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except sr.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data


def execute_command_with_name(command_name: str):
    """
    Выполнение заданной пользователем команды с дополнительными аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в функцию
    :return:
    """
    # command = command_name.split(" ")[0]

    for key in commands_list.keys():
        for el in key:
            lenght = len(el.split(" "))
            if command_name.startswith(el):
                args = [str(input_part) for input_part in voice_input.split(" ")[lenght:len(voice_input)]]
                return commands_list[key](args)
    return None


if __name__ == "__main__":
    micro = sr.Microphone()
    recognize = sr.Recognizer()

    while True:
        voice_input = speech_to_text()
        print(voice_input)

        execute_command_with_name(voice_input)
