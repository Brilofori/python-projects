"""
Windows Security Event Log Reader

Purpose:
- Programmatically access Windows Security Event Logs using pywin32
- Extract and display core metadata for security-relevant events
- Serve as a foundation for SOC-style log analysis and detection logic

Key Notes:
- Requires Administrator privileges to access the Security log
- Uses backwards sequential reading to process most recent events first
- Designed to be extended with filtering, aggregation, and alert logic W

Author: Bril Ofori
"""



import win32evtlog
import win32evtlogutil
import datetime 


def get_security_logs():
    """
    Opens a handle to the local Windows Security Event Log.

    Security Context:
    - Accessing the Security log requires elevated (Administrator) privileges
    - Failure to run as admin will result in access errors or empty reads

    Returns:
    - Event log handle used for subsequent read operations
    """
    server = 'localhost'
    logtype = 'Security'
    hand = win32evtlog.OpenEventLog(server, logtype)

    if logtype:
        print(f'sucessfully retreived {logtype} information')
    return hand 

hand = get_security_logs()

def display_event_metadata(event):
    """
    Extracts and displays core metadata from a Windows event record.

    Notes:
    - EventID is masked to remove severity bits and match standard Windows IDs (I thank stack overflow)
    - TimeGenerated is formatted for human-readable triage output

    This function isolates presentation logic from log retrieval.
    """
    event_id = event.EventID & 0xFFFF
    time = event.TimeGenerated.Format()

    print(f'Event ID: {event_id}')
    print(f'Source: {event.SourceName}')
    print(f'Time Generated: {time}')
    print('-' * 40)


def read_security_log_events():
    """
    Iterates through the Windows Security Event Log and processes events.

    Implementation Details:
    - Reads logs backwards to prioritize recent activity
    - Uses sequential reads for efficient traversal
    - Designed to support future filtering (e.g., failed logons, process creation)

    This function represents the core log ingestion loop.
    """

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

###README
### Why this project exists
###This script was built to deepen my understanding of:
###- Windows event logging internals
###- Security telemetry ingestion
###- Python automation for SOC and Blue Team workflows

