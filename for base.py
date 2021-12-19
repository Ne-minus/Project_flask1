import sqlite3

connection = sqlite3.connect('datab.db')
cur = connection.cursor()
cur.execute("""
CREATE TABLE users (
    user_id TEXT AUTO_INCREMENT, 
    name TEXT, 
    age INT,
    PRIMARY KEY (user_id)
)
""")
cur.execute("""
CREATE TABLE answers (
    user_id INT, 
    answer1 TEXT, 
    answer2 TEXT,
    PRIMARY KEY (user_id)
)
""")
cur.execute("""
CREATE TABLE questions (
    quest_id INT, 
    question_itself TEXT, 
    PRIMARY KEY (quest_id)
)
""")
connection.commit()