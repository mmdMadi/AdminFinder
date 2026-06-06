from requests import get
from colorama import Fore, Style, init
import os
import time

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0'
try: 
    init()

    good_list = []

    # -------- banner --------
    banner = r"""
        ___      _           _         ______ _           _           
    / _ \ ___| |__   ___ | |_ ___  |  ____(_)_ __   __| | ___ _ __ 
    | | | / __| '_ \ / _ \| __/ _ \ | |__  | | '_ \ / _` |/ _ \ '__|
    | |_| \__ \ | | | (_) | ||  __/ |  __| | | | | | (_| |  __/ |   
    \___/|___/_| |_|\___/ \__\___| |_|    |_|_| |_|\__,_|\___|_|   

                    ADMIN PAGE FINDER
    """

    print(Fore.CYAN + banner + Style.RESET_ALL)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    # ------------------------

    target_url = input('enter target url : ')
    target_url += '/' if not target_url.endswith('/') else ''

    paths_file = open('wordlist.txt', 'r', encoding='UTF-8')
    paths = paths_file.readlines()
    paths_file.close()

    clean_paths = []

    for line in paths:
        if line.strip() == '' or line.startswith('#'):
            continue

        line = line.strip().lstrip('/')
        clean_paths.append(line)


    for path in clean_paths:
        url = target_url + path

        try:
            req = get(url, timeout=8,userAgent=userAgent)
            status_code = req.status_code

            if status_code == 200:
                print(Fore.GREEN + f'tested url {url} and the status code is {status_code}')
                good_list.append(url)
            else:
                print(Fore.RED + f'tested url {url} and the status code is {status_code}')

        except Exception as e:
            print(Fore.YELLOW + f'error for {url} : {e}')


    print(Style.RESET_ALL)

    if len(good_list) > 0:
        print(Fore.GREEN + f'\n[+] Found {len(good_list)} possible admin page(s):\n')

        for url in good_list:
            print(Fore.GREEN + f'[+] {url}')

        # save to file
        with open('./goods.txt', 'w', encoding='utf-8') as f:
            for url in good_list:
                f.write(url + '\n')

        print(Fore.CYAN + '\n[+] All good URLs saved to ./goods.txt')

    else:
        print(Fore.RED + '\n[-] We couldn`t find any admin pages.')

    input('\npress any key to exit')


except KeyboardInterrupt:
    print(Fore.RED + 'the Application Stopped by the user .')