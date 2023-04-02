import datetime
import random
import sys
import time

import google
import googletrans
import webbrowser
from typing import Union

import wikipedia
import wikipediaapi
import requests
import pasgen
import tts
import pyjokes
from anecAPI import anecAPI


def google_search(*args) -> None:
    req_url = "http://www.google.com/search?q="

    webbrowser.open(req_url + " ".join(args[0]), 2, True)
    return None


def youtube_search(*args) -> None:
    req_url = "https://www.youtube.com/results?search_query="

    webbrowser.open(req_url + " ".join(args[0]), 2, True)
    return None


def wiki_search(*args) -> None:
    req_url = "https://ru.wikipedia.org/wiki/"

    webbrowser.open(req_url + " ".join(args[0]), 2, True)

    return None


def hi(*args):
    answer = ["Привет!", "Здравствуйте", "Слушаю"]
    tts.talk(random.choice(answer), True)


def ctime(*args):
    tts.talk("Сейчас: " + str(datetime.datetime.now().strftime("%H:%M:%S")), is_print=True)


def joke(*args):
    tts.talk(anecAPI.random_joke(), is_print=True)


def btc_price(*args):
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&precision=0')
    data = response.json()
    response.close()
    price = str(data['bitcoin']['usd']) + "$"
    tts.talk(price, True)


def exit(*args):
    tts.talk("Пока!")
    # time.sleep(1)
    sys.exit()


# TODO: BTC price, random,

# Tests
if __name__ == "__main__":
    google_search("search hello world 123 12312 22")
