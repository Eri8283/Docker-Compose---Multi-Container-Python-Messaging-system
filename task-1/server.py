from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Mary had a little lamb.")

if __name__ == "__main__":
    HTTPServer(("", 80), Handler).serve_forever()
