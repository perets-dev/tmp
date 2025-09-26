import http.client
import os
import logging
import json

from http.server import HTTPServer, BaseHTTPRequestHandler


logging.basicConfig(
    level=logging.DEBUG,
    filename='logging.log',
    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]'
)


class SimpleInterceptor(BaseHTTPRequestHandler):
    

    def do_GET(self):
        self.forward_request('GET')
    
    def do_POST(self):
        self.forward_request('POST')
    
    def do_PUT(self):
        self.forward_request('PUT')
    
    def do_DELETE(self):
        self.forward_request('DELETE')
    
    def forward_request(self, method):
        # Print request info
        logging.info(f"\n=== {method} {self.path} ===")
        logging.info(f"Headers: {json.dumps(dict(self.headers), ensure_ascii=False, indent=2)}")
        
        # Read body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else b''
        if body:
            logging.info(f"Body: {json.dumps(json.loads(body.decode()), ensure_ascii=False, indent=2)}")
        
        forward_port = int(os.getenv('FORWARD_PORT', 8090))
        conn = http.client.HTTPConnection('localhost', forward_port)
        conn.request(method, self.path, body, dict(self.headers))
        response = conn.getresponse()
        
        # Send response back to client
        self.send_response(response.status)
        for header, value in response.getheaders():
            self.send_header(header, value)
        self.end_headers()
        self.wfile.write(response.read())


if __name__ == '__main__':
    interceptor_port = int(os.getenv('INTERCEPTOR_PORT', 7125))
    server = HTTPServer(('0.0.0.0', interceptor_port), SimpleInterceptor)
    logging.info(f"Interceptor running on http://localhost:{interceptor_port}")
    server.serve_forever()
