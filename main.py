import tornado.ioloop
import tornado.web
import MySQLdb as mydb
import os.path
import Settings

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class Application(tornado.web.Application):
    """
    The tornado application  class
    """

    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = {
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
            "debug": Settings.DEBUG,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
