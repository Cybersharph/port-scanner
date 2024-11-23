import sys
import socket
from datetime import datetime

# Check if an IP address is provided as an argument
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Resolve hostname to IP
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 port-scanner.py <ip>")
    sys.exit()

# Display scan information
print("-" * 50)
print("Scanning target: " + target)
print(f"Time started: {datetime.now()}")
print("-" * 50)

def program_exit():
    print("\nExiting program.")
    print(f"Time ended: {datetime.now()}")
    print("-" * 50)
    sys.exit()

# Scan ports
try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
        socket.setdefaulttimeout(1)  # Set timeout for connections
        result = s.connect_ex((target, port))  # Attempt to connect

        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        s.close()  # Close socket after checking the port

# Handle user interruption
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
    program_exit()

# Handle hostname resolution error
except socket.gaierror:
    print("Hostname could not be resolved.")
    program_exit()

# Handle server connection error
except socket.error:
    print("Couldn't connect to server.")
    program_exit()

program_exit()
