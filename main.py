from requests import Session
from colorama import Fore, Style, init
import threading
from queue import Queue

init()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Connection": "close"
}

session = Session()
session.headers.update(headers)

good_list = []
lock = threading.Lock()
q = Queue()


def check_url(url):
    try:
        req = session.get(url, timeout=8)
        status = req.status_code

        if status == 200:
            print(Fore.GREEN + f"[200] {url}")
            with lock:
                good_list.append(url)
        else:
            print(Fore.RED + f"[{status}] {url}")

    except Exception as e:
        print(Fore.YELLOW + f"[ERR] {url} : {e}")


def worker():
    while True:
        url = q.get()
        if url is None:
            break
        check_url(url)
        q.task_done()


banner = r"""
ADMIN FINDER
"""
print(banner)

target_url = input("target url: ")
if not target_url.endswith("/"):
    target_url += "/"

with open("wordlist.txt", "r", encoding="utf-8") as f:
    paths = f.readlines()

for p in paths:
    q.put(target_url + p.strip())

threads = []
THREAD_COUNT = 50

for _ in range(THREAD_COUNT):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in threads:
    q.put(None)

for t in threads:
    t.join()

if good_list:
    print("\nFOUND:")
    for u in good_list:
        print(u)
else:
    print("NOT FOUND")