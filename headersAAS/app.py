import json
import logging
from tornado.options import options, define

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.log import enable_pretty_logging
enable_pretty_logging()


class MainHandler(tornado.web.RequestHandler):
	
	def get(self):
		header_dict = {}
		for (k,v) in self.request.headers.get_all():
			header_dict[k] = v
		self.write(header_dict)


def main():
	application = tornado.web.Application([
		(r"/", MainHandler),
	])
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)

	logging.info("Starting header service")

	tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	main()