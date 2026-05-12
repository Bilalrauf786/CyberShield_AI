from scapy.all import sniff, IP
import datetime

print("🔥 CyberShield AI - LIVE MODE STARTED")

def detect_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        time = datetime.datetime.now()

        print(f"[{time}] {ip_src} → {ip_dst}")

# LIVE network sniffing
sniff(prn=detect_packet, store=False)