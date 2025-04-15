import asyncio
import shelve
from bleak import BleakScanner
from time import strftime, gmtime, sleep

async def scan_for_devices():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Device Name: {device.name}, Address: {device.address}")
    return devices

KNOWN_DEVICES = {
    ""
}

async def check_for_known_devices():
    devices = await BleakScanner.discover()
    nearby_known_devices = {}

    for device in devices:
        if device.address in KNOWN_DEVICES.values():
            device_name = [name for name, addr in KNOWN_DEVICES.items() if addr == device.address][0]
            print(f"{device_name} is nearby!")
            nearby_known_devices[device_name] = device.address

    return nearby_known_devices

def main():
    # asyncio.run( scan_for_devices() )
    while True:
        print("Scanning...")
        asyncio.run(scan_for_known_devices())  # Replaced scan() with scan_for_known_devices()
        print("sleeping till next loop...")
        sleep(15)
        # This is the verifying portion
        print("Verifying log...")
        with shelve.open("device_log") as db:
            for name, address in db.items():
                print(f"{name}: {address}")

if __name__ == '__main__':
    main()