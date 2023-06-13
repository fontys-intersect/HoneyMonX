import http.server
import socketserver
import subprocess
import threading
import time

def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("",44444), Handler) as httpd:
        print("HTTP server running on port 44444...")
        httpd.serve_forever()

def last_line(filename):
    try:
         with open(filename, 'r') as file:
            lines = file.readlines()
            if lines:
                return lines[-1].strip()
            else:
                return "kur"
    except:
         return "69,69,69"

def generate_html():
    template_path = "template.html"
    output_path = "dynamic.html"
    with open(template_path, "r") as template_file:
        template = template_file.read()
    modified_template = template.replace("{{data}}", last_line("/home/student/data/symb.txt"))

    with open(output_path, "w") as output_file:
        output_file.write(modified_template)

if __name__=="__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    generate_html()
