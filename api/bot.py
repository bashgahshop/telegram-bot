from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        length = int(self.headers["Content-Length"])

        body = self.rfile.read(length)

        update = json.loads(body)

        print(update)

        self.send_response(200)

        self.end_headers()

        self.wfile.write(b"OK")