# PyLab010 - Bluetooth Logger (Week 12 Lab)

This is a Python lab project using `bleak` to scan for BLE (Bluetooth Low Energy) devices. It also uses `asyncio` for scanning and `shelve` from Chapter 13 for persistent storage. In addition, I used Chapter 12’s `.txt` file writing to create a readable log that can be tracked in GitHub.

## Summary

- Scans for nearby BLE devices like my Pixel 9 and tablet
- Logs timestamps when a known device is detected
- Stores logs in both `shelve` and `.txt` format
- Tagged unknown devices like speakers and TVs are also shown for reference

## How to Run

1. Make sure `bleak` is installed using `pip install bleak`
2. Run `Week12.py` in PyCharm
3. The script will scan every 15 seconds and print results
4. Logs are saved to:
    - `device_log` (persistent storage)
    - `device_log_readable.txt` (GitHub-friendly text file)

## Chapters Covered

- Chapter 12: Writing to `.txt` files
- Chapter 13: Using `shelve` for persistent data

## Author

Chris Shortt  
CIS - College of the Redwoods  
GitHub: [https://github.com/cshorr](https://github.com/cshorr)
