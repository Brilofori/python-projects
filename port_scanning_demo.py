""" with the understanding of sockets and how they are utilized within many applications and network 
functionalities, i wanted to build script that reads that checks a handlful of common ports, i reduced to the 
scope for the sake of functionality due to pythons performance hindering when scanning thousands of ports
"""

import socket
import datetime

    # Targeted high-risk ports (intentionally scoped for performance and relevance)
vulnerable_ports = {

    # Remote Access and Authentication Services
    21:  "FTP  – Clear-text authentication, credential exposure risk",
    22:  "SSH  – Brute-force and credential abuse target",
    23:  "Telnet – Legacy clear-text remote access",

    # Email Services
    25:  "SMTP – Open relay and user enumeration risk",

    # Web Services
    80:  "HTTP  – Unencrypted web service, common initial access vector",
    443: "HTTPS – Web application exposure",
    8080:"HTTP-Alt – Frequently used for admin panels and test services",

    # Windows / Enterprise Services
    3389:"RDP  – High-risk remote access, frequent brute-force target",
    445: "SMB  – Lateral movement, ransomware propagation",
    389: "LDAP – Directory enumeration and credential harvesting",

    # Database Services
    3306:"MySQL – Database exposure and data exfiltration risk",
    1433:"MSSQL – Enterprise database access, privilege escalation risk"
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
# Scan selected TCP ports and report open/closed status
def scan_ports(host_ip, ports):
    for port, description in ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host_ip, port))

        if result == 0:
            print(f"[+] Port {port} ({description}) is open")
        else:
            print(f"[-] Port {port} ({description}) is closed")
        s.close()

if validate_address(host_ip):
    scan_ports(host_ip, vulnerable_ports)
else:
    print("Invalid IPv4 address. Scan aborted.")
