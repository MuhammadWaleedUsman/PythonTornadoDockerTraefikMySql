from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import torn
import logging

from routes import *
settings = dict(
		debug=torn.Debug(),
	)

application = Application(route, **settings)

if __name__ == "__main__":
	logging.basicConfig(handlers=[logging.FileHandler('example.log'), logging.StreamHandler()],
						format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
						datefmt='%Y-%m-%d:%H:%M:%S',
						level=logging.DEBUG)
	server = HTTPServer(application)
	server.listen(torn.Port())
	IOLoop.current().start()
