# ARPSpoofingDetector

## Description
This Python script detects ARP (Address Resolution Protocol) Spoofing attacks in a network environment. Developed as the final project for a university course, it aims to demonstrate the practical application of network security principles. ARP Spoofing, or ARP Poisoning, is a malicious technique used to intercept or modify data on a local area network (LAN) by associating the attacker's MAC address with the IP address of a legitimate network host.

## Features
1. Real-time detection of ARP Spoofing attacks by monitoring the ARP table.
2. Automatic logging of detected ARP Spoofing events with timestamps.
3. Simple and easy-to-use command-line interface.

## Academic Context
This script was created as part of the coursework for Cybersecurity Bootcamp at the University of Colorado at Boulder. It is intended for educational purposes and demonstrates the implementation of network security techniques.

## Requirements
* Python 3.x
* Operating System: The script is designed to run on systems where the arp -a command is available (commonly Unix-like systems).

## Installation
No additional libraries are required to run this script as it uses built-in Python modules and system commands.

## Usage
Run the script in a Python environment. It will continuously monitor the network's ARP table and log any detected ARP Spoofing events.

```bash
python arp_spoofing_detector.py
```

## How it Works
* The script extracts the current ARP table using the arp -a command.
* It then analyzes the table for duplicate MAC addresses, which are indicative of ARP Spoofing.
* If a duplicate MAC address is found, it logs the event with the offending MAC address and timestamp in log.txt.

## License
This script is released under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

