from scapy.all import sniff, IP
import time

print("🔥 CyberShield AI - Live Packet Capture Started")

def process_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        print(f"[LIVE] {ip_src} → {ip_dst} | Protocol: {proto}")

# Start sniffing (LIVE TRAFFIC)
sniff(prn=process_packet, store=False)