# token-grabber-analysis

![Python](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square)
![Purpose](https://img.shields.io/badge/Purpose-Defense--analysis-E65100?style=flat-square)

> **SAMPLE** Discord token-stealer malware preserved strictly for defensive analysis.

> [!IMPORTANT]
> This is a **known malware family**. It is not functional software and must **NEVER** be run,
> distributed, or repurposed. It exists only to be studied for defense: detection, IoCs,
> and decryption internals.

---

## What it is

`main.py` is a classic Discord token-grabber sample. Its original behavior:

1. **Harvests tokens** - reads Discord/browser token stores under `%LOCALAPPDATA%` / `%APPDATA%`
   (Discord, Discord Canary, Lightcord, Opera, Edge, Chrome, Brave, Yandex, ...)
2. **Decrypts local DBs** - uses Windows DPAPI (`win32crypt.CryptUnprotectData`) + AES-GCM
   (`Crypto.Cipher.AES`) against the Chrome cookie/token databases
3. **Collects host metadata** - HWID via `wmic csproduct get uuid`, public IP via `api.ipify.org`
4. **Exfiltrates** - POSTs the assembled payload to a remote endpoint

---

## Analysis notes

- The outbound webhook / API URL is **intentionally blanked** in this copy.
- Request-based token checking and other gated functionality is **removed or neutralized**.
- Use **offline**, in a **disposable VM with the network cut**, for IoC extraction only.

---

## Why this exists here

Keeping a sanitized copy allows defenders to:

- Extract Indicators of Compromise (IoCs) for detection rules
- Study Windows DPAPI / AES-GCM decryption flows
- Understand the persistence of this malware family

---

## Disclaimer

This repository contains **malicious code for analysis purposes only**. Downloading, executing,
or modifying this sample for any reason other than defensive research is strongly discouraged and
may be illegal in your jurisdiction. You are solely responsible for lawful use.
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A