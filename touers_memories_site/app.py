from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import webbrowser
import threading

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8000

class SiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

def open_browser():
    webbrowser.open(f"http://{HOST}:{PORT}")

if __name__ == "__main__":
    print("Touer's Memories is running.")
    print(f"Open: http://{HOST}:{PORT}")
    threading.Timer(1.0, open_browser).start()
    try:
        ThreadingHTTPServer((HOST, PORT), SiteHandler).serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
