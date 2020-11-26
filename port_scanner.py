#!/usr/bin/env python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 port_scanner.py <IP>")

#Add pretty banner
print("-"* 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-"* 50)

try:
        for port in range(1,65536):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port)) #Returns an error indicator, 0 if the port is open, 1 if it's closed
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCouldn't connect to server.")
    sys.exit()
