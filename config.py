import commands

__ver__ = "beta 0.2"

name = "Sergey"
sex = "M"
speech_language = "RU"
recognition_language = "RU"

commands_list = {
    ("hello", "hi", "morning", "привет"): commands.hi,
    ("bye", "goodbye", "quit", "exit", "stop", "пока"): None,
    ("search", "google", "find", "найди", "найти", "иди"): commands.google_search,
    ("video", "youtube", "watch", "видео", "включи"): commands.youtube_search,
    ("wikipedia", "definition", "about", "определение", "википедия", "расскажи про",
     "расскажи о"): commands.wiki_search,
    ("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): None,
    ("language", "язык"): None,
    ("weather", "forecast", "погода", "прогноз"): None,
    ("сколько время", "который час"): commands.ctime,
    ("расскажи шутку", "расскажи анекдот", "ты знаешь анекдоты", "Пошути"): commands.joke,
}
