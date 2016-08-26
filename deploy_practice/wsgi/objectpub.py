from paste.request import parse_formvars
import threading

webinfo = threading.local()


"""
According to the WSGI protocol, web server packages up the request in the environ variable and invokes the
    application once per request with the environ and start_response objects as args.

Basic Implementation of start_response:
def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    # Re-raise original exception if headers sent
                    raise exc_info[0], exc_info[1], exc_info[2]
            finally:
                exc_info = None     # avoid dangling circular ref
        elif headers_set:
            raise AssertionError("Headers already set!")

        headers_set[:] = [status, response_headers]
        return write
"""


class ObjectPublisher(object):
    # Parses a URL and selects the right object to call (with form variables, if applicable)

    def __init__(self, root):
        self.root = root

    def __call__(self, environ, start_response):
        # Fields are now collected (parse form vars) in the request init method
        webinfo.request = Request(environ)
        webinfo.response = Response()
        obj = self.find_object(self.root, environ)
        response_body = obj(**dict(webinfo.request.fields))
        # Stock headers are now supplied in the Response init method
        start_response('200 OK', [(v, k) for k, v in webinfo.response.headers.headeritems()])
        return [response_body]

    def find_object(self, obj, environ):
        path_info = environ.get('PATH_INFO', '')
        if not path_info or path_info == '/':
            # We've arrived!
            return obj
        # PATH_INFO always starts with a /, so we'll get rid of it:
        path_info = path_info.lstrip('/')
        # Then split the path into the "next" chunk, and everything after it ("rest"):
        # Second arg to split is max splits
        parts = path_info.split('/', 1)
        next = parts[0]
        if len(parts) == 1:
            rest = ''
        else:
            rest = '/' + parts[1]
        # Hide private methods/attributes:
        assert not next.startswith('_')
        # Now we get the attribute; getattr(a, 'b') is equivalent
        # to a.b...
        # Welcome method of root object is chosen here (next is 'welcome' after parsing the path_info
        next_obj = getattr(obj, next)
        # Now fix up SCRIPT_NAME and PATH_INFO...
        environ['SCRIPT_NAME'] += '/' + next
        environ['PATH_INFO'] = rest
        # and now parse the remaining part of the URL...
        return self.find_object(next_obj, environ)


# This is just a dictionary-like object that has case-
# insensitive keys:
from paste.response import HeaderDict


class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self.fields = parse_formvars(environ)


class Response(object):
    def __init__(self):
        self.headers = HeaderDict(
            {'content-type': 'text/html'})


