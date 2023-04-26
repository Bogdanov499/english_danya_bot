from const import bot, words_db, lessons_db, stuff_db
import db

def write_word(message) :
    msg = bot.send_message(message.from_user.id, "Отправьте слово и его перевод в виде : Слово перевод")
    bot.register_next_step_handler(msg, write_word_handler)

def write_word_handler(message) :
    word, translation = message.text.split(" ")
    db.add_word(message.from_user.id, word, translation)
    bot.send_message(message.from_user.id, "Слово записано")

def get_all_words(message) :
    text = db.all_words(message.from_user.id)
    if len(text) == 0 :
        bot.send_message(message.from_user.id, "Еще не записано ни слова")
    else :
        for i in text :
            bot.send_message(message.from_user.id, ": ".join(i))

def get_translation(message) :
    msg = bot.send_message(message.from_user.id, "Напишите слово")
    bot.register_next_step_handler(msg, translation_handler)

def translation_handler(message) :
    text = db.translate(message.from_user.id, message.text)
    if len(text) == 0 :
        bot.send_message(message.from_user.id, "Еще не было этого слова")
    else :
        for i in text :
            bot.send_message(message.from_user.id, ": ".join(i))

def write_lesson(message) :
    msg = bot.send_message(message.from_user.id, "Отправьте дату урока в виде : dd-mm-yyyy")
    bot.register_next_step_handler(msg, write_lesson_date_handler)

def write_lesson_date_handler(message) :
    date = message.text
    msg = bot.send_message(message.from_user.id, "Отправьте темы урока")
    bot.register_next_step_handler(msg, write_lesson_topics_handler, date)

def write_lesson_topics_handler(message, date) :
    topics = message.text
    msg = bot.send_message(message.from_user.id, "Отправьте оценку сложности")
    bot.register_next_step_handler(msg, write_lesson_dificulty_grade_handler, date, topics)

def write_lesson_dificulty_grade_handler(message, date, topics) :
    grade = message.text
    db.add_lesson(message.from_user.id, date, topics, grade)
    bot.send_message(message.from_user.id, "Урок записан")

def get_all_lessons(message) :
    text = db.all_lessons(message.from_user.id)
    if len(text) == 0 :
        bot.send_message(message.from_user.id, "Еще не записано ни одного урока")
    else :
        for i in text :
            bot.send_message(message.from_user.id, f"Дата : _{i[0]}_\nТемы : {i[1]}\nОценка сложности : *{i[2]}*", parse_mode="Markdown")

def get_lessons_by_date(message) :
    msg = bot.send_message(message.from_user.id, "Напишите дату в виде : dd-mm-yyyy")
    bot.register_next_step_handler(msg, lesson_by_date_handler)

def lesson_by_date_handler(message) :
    text = db.lesson_by_date(message.from_user.id, message.text)
    if len(text) == 0 :
        bot.send_message(message.from_user.id, "Еще не записано ни одного урока на эту тему")
    else :
        for i in text :
            bot.send_message(message.from_user.id, f"Дата : _{i[0]}_\nТемы : {i[1]}\nОценка сложности : *{i[2]}*", parse_mode="Markdown")

def write_stuff(message) :
    msg = bot.send_message(message.from_user.id, "Отправьте название")
    bot.register_next_step_handler(msg, write_stuff_name_handler)
    
def write_stuff_name_handler(message) :
    name = message.text
    msg = bot.send_message(message.from_user.id, "Отправьте оценку материала")
    bot.register_next_step_handler(msg, write_stuff_grade_handler, name)

def write_stuff_grade_handler(message, name) :
    grade = message.text
    msg = bot.send_message(message.from_user.id, "Отправьте сслыку (если нет, то отправьте -)")
    bot.register_next_step_handler(msg, write_stuff_href_handler, name, grade)

def write_stuff_href_handler(message, name, grade) :
    href = message.text
    if href == "-" :
        href = None
    db.add_stuff(message.from_user.id, name, grade, href)
    bot.send_message(message.from_user.id, "Материал записан")

def get_stuff(message) :
    text = db.stuff(message.from_user.id)
    if len(text) == 0 :
        bot.send_message(message.from_user.id, "Еще не записано материалов")
    else :
        for i in text :
            if i[2] == None :
                bot.send_message(message.from_user.id, f"Название : {i[0]}\nОценка : *{i[1]}*", parse_mode="Markdown")
            else :
                bot.send_message(message.from_user.id, f"Название : [{i[0]}]({i[2]})\nОценка : *{i[1]}*", parse_mode="Markdown")

def clear_words(message) :
    db.clear(message.from_user.id, words_db)

def clear_lessons(message) :
    db.clear(message.from_user.id, lessons_db)

def clear_stuff(message) :
    db.clear(message.from_user.id, stuff_db)