import os
import socket

# IP Checking 
def check_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 0))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(0.2)
    try:
        # This is typically a placeholder to simulate receiving data
        message, address = s.recvfrom(8192)
        return address[0]
    except socket.timeout:
        return None

# Blacklisted IP Addresses
blocked_ips = {}

# Blocking IP Addresses
def block_ip(ip_address):
    os.system("iptables -A INPUT -s " + ip_address + " -j DROP")
    blocked_ips[ip_address] = True

while True:
    ip_address = check_ip()
    if ip_address and ip_address not in blocked_ips:
        block_ip(ip_address)
