from collections import defaultdict
from scapy.layers.inet import IP, TCP
from database.db import insert_alert

# प्रत्येक Source IP ने Scan केलेले Ports
scan_tracker = defaultdict(set)

# Alert Threshold
PORT_THRESHOLD = 10


def detect_port_scan(packet):

    if not packet.haslayer(IP):
        return

    if not packet.haslayer(TCP):
        return

    tcp = packet[TCP]

    # फक्त SYN Packet तपासा
    if tcp.flags != "S":
        return

    src_ip = packet[IP].src
    dst_port = tcp.dport

    scan_tracker[src_ip].add(dst_port)

    port_count = len(scan_tracker[src_ip])

    print(f"[SCAN] {src_ip} -> {dst_port} ({port_count})")

    if port_count >= PORT_THRESHOLD:

        print(f"[ALERT] Port Scan Detected : {src_ip}")

        insert_alert(
            "Port Scan",
            src_ip
        )

        # पुन्हा मोजणी सुरू करा
        scan_tracker[src_ip].clear()
