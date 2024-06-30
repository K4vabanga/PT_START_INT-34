import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'200\nOK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404\nNot Found')

if __name__ == '__main__':
    server_class = HTTPServer
    handler_class = Handler
    port = 8080
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'HTTP Server started on port {port}...')
    httpd.serve_forever()