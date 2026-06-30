from collections import defaultdict
from scapy.layers.inet import IP, TCP
from database.db import insert_alert

# SYN Packet Counter
syn_count = defaultdict(int)

# Alert Threshold
THRESHOLD = 20


def detect_syn_flood(packet):

    if not packet.haslayer(IP):
        return

    if not packet.haslayer(TCP):
        return

    tcp = packet[TCP]

    # Detect only SYN packet (not ACK, FIN, etc.)
    if tcp.flags == "S":

        src_ip = packet[IP].src

        syn_count[src_ip] += 1

        print(f"[SYN] {src_ip} -> {syn_count[src_ip]}")

        if syn_count[src_ip] >= THRESHOLD:

            print(f"[ALERT] SYN Flood Detected : {src_ip}")

            insert_alert(
                "SYN Flood",
                src_ip
            )

            # Reset counter after alert
            syn_count[src_ip] = 0
