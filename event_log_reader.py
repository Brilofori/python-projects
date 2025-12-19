"""
Basic Windows Event Log reader using win32evtlog.

Purpose:
- Open the System event log on a local Windows machine
- Read recent event records
- Print raw PyEventLogRecord objects for exploration

This script is for learning how Windows event logs can be accessed
programmatically for security monitoring and analysis.
"""


import win32evtlog
import datetime 

def get_security_logs():
    server = 'localhost'
    logtype = 'system'
    global hand 
    hand = win32evtlog.OpenEventLog(server, logtype)
    if logtype:
        print(f'sucessfully retreived {logtype} information')
    else:
        print(f'error with {logtype} format retreival')
    return hand 
get_security_logs()

def this_function_reads_and_stores_log_data():
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    offset = 0 
    events = win32evtlog.ReadEventLog(hand, flags, offset )
this_function_reads_and_stores_log_data()
