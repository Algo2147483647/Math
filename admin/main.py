import http.server
import socketserver
from html.readMarkdown import *
from html.drawGraph import *
import urllib.parse

PORT = 1010
abs_path = os.path.abspath(__file__).replace('\\', '/').split("/main.py")[0]

def initial():
    readMarkdown("note/")
    dg = DrawGraph()
    dg.drawTree("", 'index.html')

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path == '/':
            initial()
        
        elif self.path.split('.')[-1] == "md":
            self.send_response(200)
            self.send_header('Content-type', 'text/markdown')
            self.end_headers()
            with open(abs_path + self.path, 'r', encoding = 'utf-8') as file:
                    content = file.read()
            self.wfile.write(content.encode())
            return 

        else:
            concept = self.path.split("/")[-1]
            dg = DrawGraph()
            dg.drawTree(urllib.parse.unquote(concept), 'index.html')

        self.path = 'index.html'
        return super().do_GET()
    

if __name__ == '__main__':
    initial()
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


