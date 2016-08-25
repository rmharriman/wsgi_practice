from objectpub import ObjectPublisher
from authmiddleware import AuthMiddleware


class Root(object):

    # The "index" method:
    def __call__(self):
        return [b'<form action="welcome">', b'Name: <input type="text" name="name">', b'<input type="submit">', b'</form>']

    def welcome(self, name):
        return 'Hello {}!'.format(name).encode('utf8')

app = ObjectPublisher(Root())

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')
