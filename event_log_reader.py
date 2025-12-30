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
import win32evtlogutil
import datetime 

def get_security_logs():
    server = 'localhost'
    logtype = 'Security'
    hand = win32evtlog.OpenEventLog(server, logtype)

    if logtype:
        print(f'sucessfully retreived {logtype} information')
    return hand 

hand = get_security_logs()

def display_event_metadata(event):
    event_id = event.EventID & 0xFFFF
    time = event.TimeGenerated.Format()

    print(f'Event ID: {event_id}')
    print(f'Source: {event.SourceName}')
    print(f'Time Generated: {time}')
    print('-' * 40)


def read_security_log_events():

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    try:
        while True:
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            if not events:
                break
        
            for event in events:
                display_event_metadata(event)

    except Exception as e:
        print(f'error occured at: {e}')
    
read_security_log_events()

