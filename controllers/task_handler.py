from .db_handler import cursor
from tornado import concurrent
import tornado.web
executor = concurrent.futures.ThreadPoolExecutor(8)


def start_task(arg):
    print("The Task has started") # Async task
    return True


def stop_task(arg):
    print("The Task has stopped")  # Async task
    return True


class HandlerStart(tornado.web.RequestHandler):

    def post(self, username):
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        user_names = []
        if users:
            keys = ("id", "name", "email")
            list_of_users = [dict(zip(keys, values)) for values in users]
            for user in list_of_users:
                user_names.append(user['name'])
            if username in set(user_names):
                flag = True
            else:
                flag = False
        else:
            flag = False
        if flag:
            executor.submit(start_task, username)
            response = "started"
        else:
            response = "User Doesn't exist"
        self.write('request accepted |' + str(username) + ' | ' + str(response))


class HandlerStop(tornado.web.RequestHandler):

    def post(self, username):
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        user_names = []
        if users:
            keys = ("id", "name", "email")
            list_of_users = [dict(zip(keys, values)) for values in users]
            for user in list_of_users:
                user_names.append(user['name'])
            if username in set(user_names):
                flag = True
            else:
                flag = False
        else:
            flag = False
        if flag:
            executor.submit(stop_task, username)
            response = "stopped"
        else:
            response = "User Doesn't exist"
        self.write('request accepted |' + str(username) + ' | ' + str(response))
