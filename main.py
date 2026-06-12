from requests import Session
from colorama import Fore, Style, init
import threading
from queue import Queue
import random
import sys

init()

headers = {
    "Connection": "close"
}

session = Session()
session.headers.update(headers)

try:
    with open("user_agents.txt", "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(Fore.RED + "Error: user_agents.txt not found in project root." + Style.RESET_ALL)
    sys.exit(1)

if not user_agents:
    print(Fore.RED + "Error: user_agents.txt is empty." + Style.RESET_ALL)
    sys.exit(1)

print(Fore.CYAN + f"Loaded {len(user_agents)} user agents from user_agents.txt" + Style.RESET_ALL)

good_list = []
lock = threading.Lock()
q = Queue()


def get_random_user_agent():
    return random.choice(user_agents)


def check_url(url):
    try:
        user_agent = get_random_user_agent()
        req = session.get(url, headers={"User-Agent": user_agent}, timeout=8)
        status = req.status_code

        with lock:
            if status == 200:
                print(Fore.GREEN + f"[200] {url}")
                print(Fore.CYAN + f"      User-Agent: {user_agent}" + Style.RESET_ALL)
                good_list.append(url)
            else:
                print(Fore.RED + f"[{status}] {url}")
                print(Fore.BLUE + f"      User-Agent: {user_agent}" + Style.RESET_ALL)

    except Exception as e:
        with lock:
            print(Fore.YELLOW + f"[ERR] {url} : {e}")


def worker():
    while True:
        url = q.get()
        if url is None:
            break
        check_url(url)
        q.task_done()


banner = (
    f"{Fore.CYAN}{Style.BRIGHT}"
    f" █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗\n"
    f"██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║\n"
    f"███████║██║  ██║██╔████╔██║██║██╔██╗ ██║\n"
    f"██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║\n"
    f"██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║\n"
    f"╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝\n"
    f"{Fore.GREEN}"
    f"███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ \n"
    f"██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗\n"
    f"█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝\n"
    f"██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗\n"
    f"██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║\n"
    f"╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝\n"
    f"{Fore.MAGENTA}  ─── Admin Panel Discovery Tool ───\n"
    f"{Fore.YELLOW}  -- made by connecting26 & mmdMadi --{Style.RESET_ALL}\n"
)
print(banner)

target_url = input("target url: ")
THREAD_COUNT = int(input("enter number for threads : "))

if not target_url.endswith("/"):
    target_url += "/"

with open("wordlist.txt", "r", encoding="utf-8") as f:
    paths = f.readlines()

for p in paths:
    q.put(target_url + p.strip())

threads = []


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
    print(Fore.GREEN + "\nFOUND:")
    for u in good_list:
        print(u)
    with open("goodlist.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(good_list) + "\n")
    print(Fore.GREEN + "Saved to goodlist.txt" + Style.RESET_ALL)
else:
    print("NOT FOUND")
