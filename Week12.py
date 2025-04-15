# Lab Summary and Conclusion:{See README.md for more information and full project documentation.}
# My devices didn't appear in the scan because they weren't advertising over BLE.
# BleakScanner only detects BLE broadcasts, not classic Bluetooth.
# To test properly, I installed nRF Connect for Mobile (Google Play) on my Pixel 9 and Tablet to simulate BLE.
# That confirmed the script and logging work when BLE is active.
# In addition to logging with shelve and keeping with the spirit of Chapter 13,
# the script also writes to a readable .txt file (as introduced in Chapter 12)
# so results can be tracked manually or committed to GitHub for version control.

import asyncio
import shelve
from bleak import BleakScanner
from time import strftime, gmtime, sleep

# Known BLE devices (advertising using nRF Connect)
KNOWN_DEVICES = {
    "Pixel 9": "08:8B:C8:5E:54:76",  # 👍🐶☎️
    "My Tablet": "E0:1F:FC:EC:A0:D2"  # 👌📱😸
}

# Tagged unknown devices (used for friendly labeling)
TAGGED_UNKNOWN_DEVICES = {
    "1C:13:38:0D:32:7E": "Bluetooth Speaker 🎵",
    "4C:6C:AC:0C:D6:A3": "Neighbor's Device 🧑‍💻",
    "60:1D:B7:04:27:98": "Smart TV or Projector 📺"
}

# Scans for nearby BLE devices and identifies known or tagged addresses
async def check_for_known_devices():
    print("Scanning for Bluetooth devices...\n")

    devices = await BleakScanner.discover()
    nearby_known_devices = {}

    for device in devices:
        mac = device.address.upper()
        name = device.name or "Unnamed"

        if mac in KNOWN_DEVICES.values():
            label = [k for k, v in KNOWN_DEVICES.items() if v == mac][0]
            print(f"[✅ FOUND] {label} is nearby! ({mac})")
            nearby_known_devices[label] = mac

        elif mac in TAGGED_UNKNOWN_DEVICES:
            print(f"[🔎 TAGGED] {TAGGED_UNKNOWN_DEVICES[mac]} - {mac}")

        else:
            print(f"[❓ UNKNOWN] {name} - {mac}")

    return nearby_known_devices

# Logs devices to persistent shelve + a readable .txt file
def log_devices(devices):
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    with shelve.open("device_log") as db:
        for name, address in devices.items():
            key = f"{name}_{address}"
            if key in db:
                db[key].append(timestamp)
            else:
                db[key] = [timestamp]

    with open("device_log_readable.txt", "a", encoding="utf-8") as log_file:
        for name, address in devices.items():
            log_file.write(f"{timestamp} - {name} ({address})\n")

    print("\n[📦] Logged devices in the shelf database and text file.\n")

# Async wrapper to run a scan and log devices
async def scan():
    nearby_devices = await check_for_known_devices()

    if nearby_devices:
        log_devices(nearby_devices)
    else:
        print("No known devices detected.\n")

# Main loop: runs scan every 15 seconds and shows current log
def main():
    while True:
        print("=" * 40)
        print("Starting Bluetooth scan...")
        asyncio.run(scan())
        print("Sleeping for 15 seconds...\n")
        sleep(15)

        print("Device log snapshot:")
        with shelve.open("device_log") as db:
            for key, timestamps in db.items():
                print(f"{key}: {timestamps}")
        print("=" * 40)
        print()

if __name__ == "__main__":
    main()

"""
[ OUTPUT AFTER ADDING MY OWN DEVICES
[🔎 TAGGED] Bluetooth Speaker 🎵 - 1C:13:38:0D:32:7E
[✅ FOUND] Pixel 9 is nearby! (08:8B:C8:5E:54:76)
[✅ FOUND] My Tablet is nearby! (E0:1F:FC:EC:A0:D2)
[🔎 TAGGED] Smart TV or Projector 📺 (T60-ID) - 60:1D:B7:04:27:98
[❓ UNKNOWN] Unnamed - 73:40:69:EE:DE:55

[📦] Logged devices in the shelf database
"""
