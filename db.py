import sqlite3

from const import words_db, lessons_db, stuff_db, path_to_db

def create_db() :
    with sqlite3.connect(path_to_db + words_db) as conn :
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS words(userid INT, word TEXT, translation TEXT);")
        conn.commit()
    with sqlite3.connect(path_to_db + lessons_db) as conn :
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS lessons(userid INT, date TEXT, topics TEXT, grade TEXT);")
        conn.commit()
    with sqlite3.connect(path_to_db + stuff_db) as conn :
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS stuff(userid INT, name TEXT, grade TEXT, herf TEXT);")
        conn.commit()

def clear(id, db) :
    with sqlite3.connect(path_to_db + db) as conn :
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {db[:-3]} WHERE userid = {id}")   
        conn.commit()     

def add_word(id, word, translation) :
    with sqlite3.connect(path_to_db + words_db) as conn :
        cur = conn.cursor()
        cur.execute(f"INSERT INTO words VALUES ({id}, '{word}', '{translation}');")
        conn.commit()

def add_lesson(id, date, topics, grade) :
    with sqlite3.connect(path_to_db + lessons_db) as conn :
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS lessons(userid INT, date TEXT, topics TEXT, grade TEXT);")
        cur.execute(f"INSERT INTO lessons VALUES ({id}, '{date}', '{topics}', '{grade}');")
        conn.commit()

def add_stuff(id, name, grade, href) :
    with sqlite3.connect(path_to_db + stuff_db) as conn :
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS stuff(userid INT, name TEXT, grade TEXT, herf TEXT);")
        cur.execute(f"INSERT INTO stuff VALUES ({id}, '{name}', '{grade}', '{href}');")
        conn.commit()

def all_words(id) :
    with sqlite3.connect(path_to_db + words_db) as conn :
        cur = conn.cursor()
        res = cur.execute(f"SELECT word, translation FROM words WHERE userid = {id}")
        return res.fetchall()

def translate(id, word) :
    with sqlite3.connect(path_to_db + words_db) as conn :
        cur = conn.cursor()
        res = cur.execute(f"SELECT word, translation FROM words WHERE userid = {id} AND word = '{word}'")
        return res.fetchall()

def all_lessons(id) :
    with sqlite3.connect(path_to_db + lessons_db) as conn :
        cur = conn.cursor()
        res = cur.execute(f"SELECT date, topics, grade FROM lessons WHERE userid = {id}")
        return res.fetchall()

def lesson_by_date(id, date) :
    with sqlite3.connect(path_to_db + lessons_db) as conn :
        cur = conn.cursor()
        res = cur.execute(f"SELECT date, topics, grade FROM lessons WHERE userid = {id} AND date = '{date}'")
        return res.fetchall()

def stuff(id) :
    with sqlite3.connect(path_to_db + stuff_db) as conn :
        cur = conn.cursor()
        res = cur.execute(f"SELECT name, grade, herf FROM stuff WHERE userid = {id}")
        return res.fetchall()