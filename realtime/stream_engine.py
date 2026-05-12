import pandas as pd
import time
import random

print("🔥 CyberShield AI - Live Traffic Stream Started")

data = pd.read_csv("dataset/cicids.csv")

while True:
    packet = data.sample(1)

    # simulate delay like real network
    time.sleep(random.uniform(0.1, 0.5))

    print("📡 Packet Stream:", packet.values[0])