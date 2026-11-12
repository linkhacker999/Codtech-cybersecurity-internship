# Task 3: Port Scanner (Python)

This is a Python tool made for the **CodTech IT Solutions Cybersecurity Internship**. It scans a target IP address or domain across a range of ports to find which ports are open and what services are running on them.

## What It Does
* Converts a domain name into an IP address using Python's `socket` library.
* Checks each port in the selected range to see if it is open.
* Identifies common service names (such as SSH, HTTP, FTP) for open ports.
* Shows the total scan time and number of open ports found.

## How to Run
1. Run this command in the terminal:
   python port_scanner.py
2. Enter a safe target (such as `127.0.0.1` or `scanme.nmap.org`), start port, and end port.

## Output Screenshot
![Output](./output.png)