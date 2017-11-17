import tornado.ioloop
import tornado.web
import MySQLdb as mydb
import os.path
import Settings
import api

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
class My404Handler(tornado.web.RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.render('404.html', errormessage='404: Page Not Found', username="")

class Application(tornado.web.Application):
    """
    The tornado application  class
    """

    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/bss/create/", api.CreateHandler),
        ]
        settings = {
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
            "debug": Settings.DEBUG,
            "cookie_secret": Settings.COOKIE_SECRET,
            "static_url_prefix": "/static/",
            "default_handler_class": "My404Handler",
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
