# from http.server import BaseHTTPRequestHandler, HTTPServer
# import sqlite3
# import urllib.parse
# import os

# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
#     def _send_response(self, content, content_type='text/html'):
#         self.send_response(200)
#         self.send_header('Content-type', content_type)
#         self.end_headers()
#         self.wfile.write(content.encode())

#     def _get_template(self, template_name):
#         with open(f'templates/{template_name}', 'r') as file:
#             return file.read()

#     def _serve_static(self, path):
#         with open(path, 'rb') as file:
#             self.send_response(200)
#             self.send_header('Content-type', 'text/css')
#             self.end_headers()
#             self.wfile.write(file.read())

#     def do_GET(self):
#         template = self._get_template('index.html')
#         if self.path.startswith('/static/'):
#             self._serve_static(self.path.lstrip('/'))
#         else:
#             if self.path == '/':
#                 conn = sqlite3.connect('database.db')
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT * FROM users")
#                 users = cursor.fetchall()
#                 conn.close()

#                 template = self._get_template('index.html')
#                 content = template.replace('{{ users }}', str(users))
#                 self._send_response(content)
#             else:
#                 self.send_response(404)
#                 self.end_headers()

#     def do_POST(self):
#         if self.path == '/add_user':
#             content_length = int(self.headers['Content-Length'])
#             post_data = self.rfile.read(content_length)
#             data = urllib.parse.parse_qs(post_data.decode())
#             username = data['username'][0]

#             conn = sqlite3.connect('database.db')
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
#             conn.commit()
#             conn.close()

#             self.send_response(302)
#             self.send_header('Location', '/')
#             self.end_headers()

# def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     print(f'Starting server on port {port}...')
#     httpd.serve_forever()

# if __name__ == '__main__':
#     run()



from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, content, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(content.encode())

    def _get_template(self, template_name):
        with open(f'templates/{template_name}', 'r') as file:
            return file.read()

    def do_GET(self):
        if self.path == '/':
            template = self._get_template('index.html')
            self._send_response(template)
        elif self.path.startswith('/static/'):
            self._serve_static(self.path.lstrip('/'))
        else:
            self.send_response(404)
            self.end_headers()

    def _serve_static(self, path):
        with open(path, 'rb') as file:
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            self.wfile.write(file.read())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
