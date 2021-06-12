from controllers.user_handler import UserHandler
from controllers.task_handler import HandlerStart, HandlerStop

route = [
    (r"/user", UserHandler),
    (r"/server/start/(.*)", HandlerStart),
    (r"/server/stop/(.*)", HandlerStop),
]
