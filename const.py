from telebot import TeleBot
import os

#TOKEN = os.environ.get("TOKEN")
TOKEN = "6294579728:AAEEpUrkIStpfe0tWyi_zFhns0ATsiJaFGc"
bot = TeleBot(TOKEN)

path_to_db = "db/"
words_db = "words.db"
lessons_db = "lessons.db"
stuff_db = "stuff.db"
