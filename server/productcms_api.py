# -*- coding: utf-8 -*-
"""
ProductSiteCMS V1.1 local save API
Windows 7 / Python 3.8 compatible
"""
import base64
import json
import os
import shutil
import socket
import subprocess
import tempfile
import threading
import time
import urllib.request
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

HOST = "0.0.0.0"
PORT = 8765
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
IMAGE_DIR = ROOT / "images"
BACKUP_DIR = DATA_DIR / "backups"
MAX_IMAGE_BYTES = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

DATA_DIR.mkdir(parents=True, exist_ok=True)
IMAGE_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)


def json_bytes(data):
    return json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")


def safe_image_name(filename):
    name = os.path.basename(str(filename or "")).strip()
    if not name:
        raise ValueError("画像ファイル名が空です")

    ext = Path(name).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError("対応していない画像形式です")

    stem = Path(name).stem
    safe_stem = "".join(c for c in stem if c.isalnum() or c in "-_")
    if not safe_stem:
        safe_stem = "game-icon-" + datetime.now().strftime("%Y%m%d%H%M%S")

    return safe_stem + ext


def atomic_write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        backup = BACKUP_DIR / (path.stem + "_" + stamp + path.suffix)
        shutil.copy2(str(path), str(backup))

    fd, temp_name = tempfile.mkstemp(
        prefix=path.name + ".",
        suffix=".tmp",
        dir=str(path.parent)
    )

    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")

        os.replace(temp_name, str(path))
    finally:
        if os.path.exists(temp_name):
            os.remove(temp_name)


GIT_CONFIG_PATH = ROOT / "server" / "git_config.json"


def load_git_config():
    default = {
        "enabled": True,
        "branch": "main",
        "remote": "origin",
        "commit_name": "ProductSiteCMS",
        "commit_email": "productsitecms@localhost"
    }

    if not GIT_CONFIG_PATH.exists():
        return default

    try:
        with open(str(GIT_CONFIG_PATH), "r", encoding="utf-8") as handle:
            loaded = json.load(handle)
        if isinstance(loaded, dict):
            default.update(loaded)
    except Exception:
        pass

    return default


def run_git(args, timeout=90):
    command = ["git"] + list(args)
    startupinfo = None

    if os.name == "nt":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    completed = subprocess.run(
        command,
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        timeout=timeout,
        startupinfo=startupinfo
    )

    output = (completed.stdout or "").strip()
    error = (completed.stderr or "").strip()

    if completed.returncode != 0:
        raise RuntimeError(error or output or "git command failed")

    return output


def get_git_status():
    config = load_git_config()

    if not config.get("enabled", True):
        return {
            "ready": False,
            "message": "git_config.jsonで無効化されています"
        }

    try:
        version = run_git(["--version"], timeout=10)
    except Exception as exc:
        return {
            "ready": False,
            "message": "Gitが見つかりません: %s" % exc
        }

    if not (ROOT / ".git").exists():
        return {
            "ready": False,
            "message": "wwwrootがGitリポジトリではありません",
            "git_version": version
        }

    remote = str(config.get("remote") or "origin")
    branch = str(config.get("branch") or "main")

    try:
        remote_url = run_git(["remote", "get-url", remote], timeout=10)
    except Exception:
        return {
            "ready": False,
            "message": "GitHub remote '%s' が未設定です" % remote,
            "branch": branch,
            "git_version": version
        }

    return {
        "ready": True,
        "branch": branch,
        "remote": remote,
        "remote_url": remote_url,
        "git_version": version
    }


def publish_to_github(commit_message):
    config = load_git_config()
    status = get_git_status()

    if not status.get("ready"):
        return {
            "ok": False,
            "error": status.get("message", "GitHub設定が完了していません")
        }

    remote = str(config.get("remote") or "origin")
    branch = str(config.get("branch") or "main")
    commit_name = str(config.get("commit_name") or "ProductSiteCMS")
    commit_email = str(config.get("commit_email") or "productsitecms@localhost")

    try:
        run_git(["config", "user.name", commit_name], timeout=10)
        run_git(["config", "user.email", commit_email], timeout=10)
        run_git(["add", "-A"], timeout=30)

        changes = run_git(["status", "--porcelain"], timeout=15)
        if not changes:
            return {
                "ok": True,
                "changed": False,
                "message": "変更なし。GitHubは最新状態です。"
            }

        message = str(commit_message or "").strip()
        if not message:
            message = "CMS update " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        run_git(["commit", "-m", message], timeout=60)
        push_output = run_git(["push", remote, branch], timeout=120)

        try:
            commit_hash = run_git(["rev-parse", "--short", "HEAD"], timeout=10)
        except Exception:
            commit_hash = ""

        return {
            "ok": True,
            "changed": True,
            "branch": branch,
            "commit": commit_hash,
            "message": push_output or "GitHub push completed"
        }

    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "error": "GitHub通信がタイムアウトしました"
        }
    except Exception as exc:
        return {
            "ok": False,
            "error": str(exc)
        }



class Handler(BaseHTTPRequestHandler):
    server_version = "ProductSiteCMS/1.1"

    def log_message(self, fmt, *args):
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-store")

    def _send_json(self, status, data):
        body = json_bytes(data)
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get("Content-Length", "0"))

        if length <= 0:
            return {}

        if length > 12 * 1024 * 1024:
            raise ValueError("送信データが大きすぎます")

        raw = self.rfile.read(length)
        return json.loads(raw.decode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/api/status":
            self._send_json(200, {
                "ok": True,
                "version": "1.1",
                "root": str(ROOT),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "git": get_git_status()
            })
            return

        self._send_json(404, {"ok": False, "error": "Not found"})

    def do_POST(self):
        path = urlparse(self.path).path

        try:
            payload = self._read_json()

            if path == "/api/upload":
                filename = safe_image_name(payload.get("filename"))
                encoded = payload.get("content_base64")

                if not isinstance(encoded, str) or not encoded:
                    raise ValueError("画像データがありません")

                try:
                    content = base64.b64decode(encoded, validate=True)
                except Exception:
                    raise ValueError("画像データを読み取れません")

                if len(content) > MAX_IMAGE_BYTES:
                    raise ValueError("画像は5MB以下にしてください")

                target = IMAGE_DIR / filename
                with open(str(target), "wb") as handle:
                    handle.write(content)

                self._send_json(200, {
                    "ok": True,
                    "filename": filename,
                    "path": "/images/" + filename,
                    "size": len(content)
                })
                return

            if path in ("/api/save", "/api/save-and-publish"):
                games = payload.get("games")
                products = payload.get("products")

                if not isinstance(games, list):
                    raise ValueError("gamesデータが不正です")

                if not isinstance(products, list):
                    raise ValueError("productsデータが不正です")

                atomic_write_json(DATA_DIR / "games.json", games)
                atomic_write_json(DATA_DIR / "products.json", products)

                response = {
                    "ok": True,
                    "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "games_count": len(games),
                    "products_count": len(products)
                }

                if path == "/api/save-and-publish":
                    response["publish"] = publish_to_github(
                        payload.get("commit_message")
                    )

                self._send_json(200, response)
                return

            self._send_json(404, {"ok": False, "error": "Not found"})

        except PermissionError:
            self._send_json(500, {
                "ok": False,
                "error": "保存権限がありません。APIを管理者として起動してください。"
            })

        except Exception as exc:
            self._send_json(400, {
                "ok": False,
                "error": str(exc)
            })



def get_lan_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "192.168.11.17"
    finally:
        sock.close()


def run_self_test():
    time.sleep(0.8)
    url = "http://127.0.0.1:%d/api/status" % PORT
    try:
        with urllib.request.urlopen(url, timeout=4) as response:
            body = response.read().decode("utf-8", errors="replace")
        print("")
        print("[SELF TEST] API OK")
        print("[SELF TEST] %s" % url)
        print("[SELF TEST] %s" % body)
        print("")
    except Exception as exc:
        print("")
        print("[SELF TEST] API FAILED")
        print("[SELF TEST] %s" % exc)
        print("")


def main():
    lan_ip = get_lan_ip()

    print("=" * 68)
    print(" ProductSiteCMS V1.1 Save API")
    print(" ROOT       : %s" % ROOT)
    print(" LOCAL TEST : http://127.0.0.1:%d/api/status" % PORT)
    print(" WIN11 TEST : http://%s:%d/api/status" % (lan_ip, PORT))
    print(" CMS        : http://%s/admin/" % lan_ip)
    print("")
    print(" IMPORTANT:")
    print("  127.0.0.1 works only on the same Win7 PC.")
    print("  From Win11, use the WIN11 TEST URL shown above.")
    print("  Keep this window open while using the CMS.")
    print("=" * 68)

    try:
        server = ThreadingHTTPServer((HOST, PORT), Handler)
    except OSError as exc:
        print("")
        print("[ERROR] Could not bind port %d." % PORT)
        print("[ERROR] %s" % exc)
        print("[ERROR] Another API may already be running.")
        input("Press Enter to close...")
        return

    threading.Thread(target=run_self_test, daemon=True).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nAPIを停止します。")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
