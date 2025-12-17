import socket
import datetime

vulnerable_ports = {
    21: "FTP",
    22: "SSH",
    23: "telnet",
    80: "HTTP",
    110: "POP3",
}

host_ip = input("Provide IPv4 address to scan: ")

def validate_address(host_ip):
    try:
        socket.inet_aton(host_ip)
        return True
    except socket.error:
        return False

def scan_port(host_ip, vulnerable_ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    for port in vulnerable_ports:
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
