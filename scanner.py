import socket
import sys
import time
from datetime import datetime

def parse_ports(port_input):
    ports = set()
    if ',' in port_input:
        parts = port_input.split(',')
        for part in parts:
            ports.update(parse_ports(part))
    elif '-' in port_input:
        start, end = port_input.split('-')
        start = int(start)
        end = int(end)
        if not (0 <= start <= 65535 and 0 <= end <= 65535):
            raise ValueError("Port numbers must be between 0 and 65535.")
        ports.update(range(start, end + 1))
    else:
        port = int(port_input)
        if not (0 <= port <= 65535):
            raise ValueError("Port numbers must be between 0 and 65535.")
        ports.add(port)
    return sorted(ports)

def scan_host(host, ports):
    print(f"[{datetime.now()}] Starting scan on {host}")
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("[ERROR] Could not resolve hostname.")
        return

    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((ip, port))
                status = "[OPEN]" if result == 0 else "[CLOSED]"
                print(f"Port {port}: {status}")
                time.sleep(0.1)  # delay to respect scanning ethics
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    print(f"[{datetime.now()}] Scan complete.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scanner.py <host> <port(s)>")
        print("Example: python scanner.py 127.0.0.1 22,80,443 or 20-25")
        sys.exit(1)

    host = sys.argv[1]
    try:
        ports = parse_ports(sys.argv[2])
        scan_host(host, ports)
    except ValueError as ve:
        print(f"[ERROR] Invalid input: {ve}")
       
time