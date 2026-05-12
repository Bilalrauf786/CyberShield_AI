from ml.detector import predict
import pandas as pd
import time
import random

data = pd.read_csv("dataset/cicids.csv")

attack_count = 0

print("🔥 SOC ENGINE RUNNING...")

for i in range(200):
    packet = data.sample(1)

    result = predict(packet.drop("Label", axis=1))

    if "ATTACK" in result:
        attack_count += 1
        print(f"🚨 ALERT #{attack_count} -> {result}")
    else:
        print(f"🟢 NORMAL TRAFFIC")

    time.sleep(0.2)