# ARP Spoofer

This is a Python-based ARP spoofing tool that allows you to perform ARP poisoning on a target device in a network. It sends spoofed ARP packets to the target and the router to intercept network traffic.

## Features

- Spoofs ARP packets to redirect traffic between a target device and a router.
- Resolves MAC addresses of devices in the network.
- Handles errors gracefully when MAC addresses cannot be resolved.
- Allows user to specify target and router IP addresses via command-line arguments.

## Requirements

- Python 3.x
- [Scapy](https://scapy.net/) library

## Installation

1. Clone this repository or download the script.
2. Install the required dependencies:
   ```bash
   pip install scapy
   ```

## Usage

Run the script with the following options:

```bash
python arp_spoofer.py -t <target_ip> -r <router_ip>
```

- `-t` or `--target`: Specify the victim's IP address.
- `-r` or `--router`: Specify the gateway/router's IP address.

### Example

```bash
python arp_spoofer.py -t 192.168.1.100 -r 192.168.1.1
```

This will start sending spoofed ARP packets to the target device (`192.168.1.100`) and the router (`192.168.1.1`).

## How It Works

1. The script resolves the MAC addresses of the target and the router using ARP requests.
2. It sends spoofed ARP responses to the target, making it believe the attacker's machine is the router.
3. It continuously sends these spoofed packets every 2 seconds to maintain the attack.

## Stopping the Script

To stop the script, press `CTRL+C`. The script will exit gracefully.

## Disclaimer

This tool is for educational purposes only. Use it responsibly and only on networks you own or have permission to test. Unauthorized use of this tool may violate laws and regulations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.