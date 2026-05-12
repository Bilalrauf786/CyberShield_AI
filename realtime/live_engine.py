import time
import random
import json

print("🔥 CyberShield AI LIVE ENGINE STARTED")

attack = 0
normal = 0

while True:
    ip = f"192.168.1.{random.randint(1,255)}"
    size = random.randint(50, 1500)

    if size > 1200:
        attack += 1
        status = "ATTACK"
    else:
        normal += 1
        status = "NORMAL"

    data = {
        "ip": ip,
        "size": size,
        "status": status,
        "attacks": attack,
        "normal": normal
    }

    # 🔥 SAVE TO FILE (BRIDGE)
    with open("realtime/live_data.json", "w") as f:
        json.dump(data, f)

    print(data)

    time.sleep(1)