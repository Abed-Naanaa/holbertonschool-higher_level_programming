import http.server
import json



class MyHandler(http.server.BaseHTTPRequestHandler):

    accepted_paths = ["/", "/data", "/info", "/status"]
    def do_GET(self):
        if self.path not in self.accepted_paths:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())
            return
        elif self.path == '/data':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"name": "John", "age": 30, "city": "New York"}).encode())

        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        
        elif self.path == '/status':
            self.send_response(200)
            self.end_headers()
            self.wfile.write("OK".encode())

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"version": "1.0", "description": "A simple API built with http.server"}).encode())

def run(server_class=http.server.HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
