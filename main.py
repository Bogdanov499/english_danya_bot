from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from const import bot
from db import create_db
import handlers

commands = {"Записать слово с переводом" : handlers.write_word,
            "Получить все записанные слова" : handlers.get_all_words,
            "Получить перевод слова" : handlers.get_translation,
            "Записать урок" : handlers.write_lesson,
            "Получить все записанные уроки" : handlers.get_all_lessons,
            "Получить уроки записанные на данную дату" : handlers.get_lessons_by_date,
            "Записать материал" : handlers.write_stuff,
            "Получить записанные материалы" : handlers.get_stuff,
            "Очистить слова" : handlers.clear_words,
            "Очистить уроки" : handlers.clear_lessons,
            "Очистить материалы" : handlers.clear_stuff
            }

@bot.message_handler(commands=["start", "help"])
def start_or_help(message) :
    keyboard = ReplyKeyboardMarkup()
    for key in commands.keys() : 
        keyboard_key = KeyboardButton(text=key)
        keyboard.add(keyboard_key)
    bot.reply_to(message, "Бот для изучения языков", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def reply(message) :
    text = message.text
    print(text)
    if text not in commands :
        bot.reply_to(message, "Неизвестная команда")
    else :
        commands[text](message)
        

if __name__ == "__main__" :
    create_db()
    bot.polling(none_stop=True, interval=0)

