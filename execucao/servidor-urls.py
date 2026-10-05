from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        target=super().translate_path(path)
        if not Path(target).suffix and Path(target+'.html').is_file():
            return target+'.html'
        return target
    def log_message(self, *args): pass

ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()
