import sqlite3

class HighScoreDB:
    def __init__(self, db_name='highscores.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS highscores (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       score INTEGER
                   );'''
        self.conn.execute(query)
        self.conn.commit()

    def insert_score(self, score):
        query_insert = '''INSERT INTO highscores (score) VALUES (?);'''
        query_delete = '''DELETE FROM highscores;'''

        cursor = self.conn.cursor()
        cursor.execute(query_delete)
        cursor.execute(query_insert, (score,))

        self.conn.commit()

    def get_highscore(self):
        query = '''SELECT MAX(score) FROM highscores;'''
        cursor = self.conn.execute(query)
        highscore = cursor.fetchone()[0]
        return highscore if highscore else 0

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    highscore_db = HighScoreDB()


    def game_over(score):
        highscore_db.insert_score(score)


    highscore = highscore_db.get_highscore()
    print("High score:", highscore)

    highscore_db.close()