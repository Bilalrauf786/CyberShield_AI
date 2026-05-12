import time
import random
import os

# Safe mode (no scapy crash)
os.environ["SCAPY_NO_CACHE"] = "1"

print("🔥 CyberShield AI - LIVE ENGINE STARTED")
print("========================================")

attack_count = 0
normal_count = 0

# Fake but realistic network sources
ips = [
    "192.168.1.10", "192.168.1.25", "10.0.0.5",
    "172.16.0.3", "8.8.8.8", "1.1.1.1"
]

protocols = ["TCP", "UDP", "HTTP", "DNS"]

while True:
    ip_src = random.choice(ips)
    ip_dst = "192.168.1.100"
    proto = random.choice(protocols)
    packet_size = random.randint(40, 1500)

    # AI-like decision simulation
    is_attack = packet_size > 1000 or random.random() > 0.85

    if is_attack:
        attack_count += 1
        status = "🚨 ATTACK DETECTED"
    else:
        normal_count += 1
        status = "🟢 NORMAL TRAFFIC"

    print(f"[{proto}] {ip_src} → {ip_dst} | Size: {packet_size} | {status}")
    print(f"Stats → Attacks: {attack_count} | Normal: {normal_count}")
    print("-" * 60)

    time.sleep(0.7)