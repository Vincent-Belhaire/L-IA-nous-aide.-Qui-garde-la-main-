#!/usr/bin/env python3
"""Ouvre le parcours sur ce poste, sans installation de module ni envoi de réponses."""
from __future__ import annotations
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent

class CourseHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        self.send_error(403, "Directory listing disabled")
        return None

    def end_headers(self):
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def log_message(self, format, *args):
        pass  # Pas de journal des consultations sur disque.

    def do_POST(self):
        self.send_error(405, "Read only")


def main() -> None:
    parser = argparse.ArgumentParser(description="Parcours IA sur ce poste seulement")
    parser.add_argument("--no-browser", action="store_true", help="Ne pas ouvrir le navigateur automatiquement")
    args = parser.parse_args()
    if not (ROOT / "index.html").is_file():
        raise SystemExit("index.html est absent : extrais tout le ZIP avant de lancer le parcours.")
    handler = partial(CourseHandler, directory=str(ROOT))
    try:
        # Port libre choisi automatiquement ; écoute uniquement sur le poste local.
        with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
            server.daemon_threads = True
            url = f"http://127.0.0.1:{server.server_port}/index.html"
            print("\nParcours IA — serveur local, lecture seule", flush=True)
            print("Adresse à ouvrir : " + url, flush=True)
            print("Garde cette fenêtre ouverte. Ctrl+C pour arrêter.", flush=True)
            print("YouTube nécessite Internet et peut être filtré par le réseau.\n", flush=True)
            if not args.no_browser:
                threading.Timer(0.5, lambda: webbrowser.open(url)).start()
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
    except OSError as exc:
        raise SystemExit(f"Impossible d’ouvrir le serveur local : {exc}") from exc

if __name__ == "__main__":
    main()
