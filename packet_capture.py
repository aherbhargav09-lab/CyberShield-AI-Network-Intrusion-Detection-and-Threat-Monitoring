from scapy.all import sniff

from detector.syn_flood import detect_syn_flood
from detector.port_scan import detect_port_scan

from database.db import update_packet_count


def process_packet(packet):

    # प्रत्येक Packet Database मध्ये Count करा
    update_packet_count()

    print(packet.summary())

    # Attack Detection
    detect_syn_flood(packet)

    detect_port_scan(packet)


def start_sniffing():

    print("[+] Packet Capture Started on eth0...")

    sniff(
        iface="eth0",
        prn=process_packet,
        store=False
    )
