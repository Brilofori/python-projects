import socket 
from datetime import datetime  
import json 
import os
import psutil


def get_ip_adress():
    ip_adresses = []
    nics = psutil.net_if_addrs()
   
    for interface_name, addresses in nics.items():
        for addr in addresses:
            if addr.family == socket.AF_INET and addr.address != '127.0.0.1':
                ip_adresses.append(addr.address)
    return ip_adresses
get_ip_adress() 

