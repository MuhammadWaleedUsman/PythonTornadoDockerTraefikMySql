import logging
from .modules import *
from .db_handler import cursor, conn
try:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users "
        "(id int NOT NULL AUTO_INCREMENT,name varchar(500),email varchar(700),PRIMARY KEY (id));")
except Exception as ex:
    pass


class UserHandler(tornado.web.RequestHandler):
    """CRUD CYCLE"""

    def get(self):
        cursor.execute("SELECT * FROM users")
        self.write(tornado.escape.json_encode(cursor.fetchall()))

    def post(self):
        record = tornado.escape.json_decode(self.request.body)
        print(record)
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (record['title'], record['body'])
        cursor.execute(sql, val)
        conn.commit()
        self.get()

    def delete(self):
        post_id = tornado.escape.json_decode(self.request.body)
        cursor.execute('DELETE FROM posts WHERE id ={}'.format(post_id['id']))
        conn.commit()
        self.get()


    def put(self):
        record = tornado.escape.json_decode(self.request.body)
        cursor.execute('UPDATE posts SET title=:title,body=:body WHERE id=:id', record)
        conn.commit()
        self.get()
