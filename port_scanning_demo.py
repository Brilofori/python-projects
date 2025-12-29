""" with the understanding of sockets and how they are utilized within many applications and network 
functionalities, i wanted to build script that reads that checks a handlful of common ports, i reduced to the 
scope for the sake of functionality due to pythons performance hindering when scanning thousands of ports
"""


import socket
import datetime

#establishing the ports i want to scan
vulnerable_ports = {
    21: "FTP",
    22: "SSH",
    23: "telnet",
    80: "HTTP",
    110: "POP3",
}

host_ip = input("Provide IPv4 address to scan: ")

#validating the adress 
def validate_address(host_ip):
    try:
        socket.inet_aton(host_ip)
        return True
    except socket.error:
        return False
#creating the socket to scan the user adress(ipv4 only) and relaying back to user if the dictionairy of
#ports is open or closed.
def scan_port(host_ip, vulnerable_ports):
    for port in vulnerable_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host_ip, port))

        if result == 0:
            print(f"[+] Port {port} ({vulnerable_ports[port]}) is open")
        else:
            print(f"[-] Port {port} ({vulnerable_ports[port]}) is closed")

        s.close()

if validate_address(host_ip):
    scan_port(host_ip, vulnerable_ports)
else:
    print("Invalid IPv4 address. Scan aborted.")
