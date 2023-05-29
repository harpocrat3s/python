#!/usr/bin/env python3

"""
This script is a port scanner that performs a sequential scan of ports on a specified IP address or hostname.
It identifies open ports by attempting to establish a TCP connection to each port.

Usage: python port_scanner.py <target_IP>

Example: python port_scanner.py 192.168.0.1
"""

import sys
import socket
from datetime import datetime

# Validate and extract the target IP address
try:
    target = socket.inet_pton(socket.AF_INET, sys.argv[1])
except (socket.error, OSError):
    print("Invalid IP address.")
    sys.exit(1)

# Add a pretty banner
print("-" * 50)
print(f"Scanning target {socket.inet_ntoa(target)}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

open_ports = set()  # Set to store open ports

# Perform port scanning
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        socket.setdefaulttimeout(1)

        for port in range(1, 65536):
            result = s.connect_ex((target, port))  # Returns an error indicator: 0 if the port is open, 1 if closed
            if result == 0:
                open_ports.add(port)

    # Print the open ports
    for port in sorted(open_ports):
        print(f"Port {port} is open")

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except (socket.gaierror, socket.error, OSError) as e:
    print(f"\nError occurred: {str(e)}")
    sys.exit()
