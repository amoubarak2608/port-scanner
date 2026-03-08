# Port Scanner

A command-line network port scanner built in Python that scans a target host for open ports and identifies running services.

## Features
- Scans ports 1-100 on any target host
- Identifies common services (SSH, HTTP, FTP, etc.)
- Displays total scan time

## How to Run
1. Make sure Python is installed
2. Clone this repo or download scanner.py
3. Run in terminal:
python scanner.py
4. Enter a hostname when prompted (e.g. scanme.nmap.org)

## Example Output
Target: scanme.nmap.org
IP Address: 45.33.32.156
Port 22 is open. Service: SSH
Port 80 is open. Service: HTTP
Scan completed in 99.08 seconds.

## Legal Notice
Only scan hosts you own or have explicit permission to scan.
scanme.nmap.org is a legal test target provided by the Nmap project.
