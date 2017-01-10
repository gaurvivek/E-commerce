import threading
import webbrowser
from wsgiref.simple_server import make_server
from chunk_try import main1
from return1 import text3
FILE = 'popup.html'
PORT = 8080

def test_app(environ, start_response):
    print "got connection"
    if environ['REQUEST_METHOD'] == 'POST':
        try:
            request_body_size = int(environ['CONTENT_LENGTH'])
            request_body = environ['wsgi.input'].read(request_body_size)
        except (TypeError, ValueError):
            request_body = "0"
            print "nothing in request"
        try:
            respose_body=''
            response_body = str(main1(str(request_body)))
            print response_body
	    print "respose created", response_body
        except:
	    print "there is error in response"
            response_body = "error"
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        request_body=''
        return [response_body]
    else:
	print "in else loop"
        response_body = open(FILE).read()
        status = '200 OK'
        headers = [('Content-type', 'text/html'),
                   ('Content-Length', str(len(response_body)))]
        start_response(status, headers)
        request_body=''
        return [response_body]

def start_server():
    """Start the server."""
    print "server started"
    httpd = make_server("", PORT, test_app)
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()
