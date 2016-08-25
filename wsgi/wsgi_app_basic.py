from paste.request import parse_formvars


def app(environ, start_response):
    fields = parse_formvars(environ)
    if environ['REQUEST_METHOD'] == 'POST':
        start_response('200 OK', [('content-type', 'text/html')])
        return [b'Hello, ', fields['name'].encode('utf8'), b'!']
    else:
        start_response('200 OK', [('content-type', 'text/html')])
        return [b'<form method="POST">Name: <input type="text" '
                b'name="name"><input type="submit"></form>']

"""
def app(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return [b'Hello world!']
"""

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')