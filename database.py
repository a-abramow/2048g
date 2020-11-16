import sqlite3

bd = sqlite3.connect("2040.sqlite")

cur = bd.cursor()

# создаем таблицу с именем RECORDS и полями name и score
cur.execute("""
create table if not exists RECORDS (  
    name text,
    score integer
)""")


# запрос с выбором и сортировкой трех лучших игроков
def get_best():          # создаем функцию с запросом для использовании в main.py
    cur.execute("""
    SELECT name gamer, max(score) score FROM RECORDS
    GROUP by name
    ORDER by score DESC
    limit 3
    """)
    return cur.fetchall()


print(get_best())            #

