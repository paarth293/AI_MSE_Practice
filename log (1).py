## Question 1 — AIOps Log Anomaly Detection
'''
You are working as an AIOps engineer for an application server. The server generates logs containing CPU usage, memory usage and response time.
Create a Python program that:

1. Creates or reads a sample dataset containing:
   - Timestamp
   - CPU Usage
   - Memory Usage
   - Response Time
2. Calculates basic statistics for the metrics.
3. Detects anomalous values using a simple threshold-based approach.
4. Prints the anomalous records.
5. Displays a graph showing the metric values and anomalies.

**Expected output:**
Total records: 20
Anomalies detected: 3

Timestamp       CPU       Status
10:05           95%      ANOMALY
10:12           97%      ANOMALY
10:18           92%      ANOMALY
**Concepts tested:**
 AIOps fundamentals, logs, metrics, anomaly detection.
 '''



import pandas as pd
import matplotlib.pyplot as plt

# 1. Create sample dataset
data = {
    "Timestamp": [
        "10:00", "10:01", "10:02", "10:03", "10:04",
        "10:05", "10:06", "10:07", "10:08", "10:09",
        "10:10", "10:11", "10:12", "10:13", "10:14",
        "10:15", "10:16", "10:17", "10:18", "10:19"
    ],

    "CPU": [
        45, 50, 52, 48, 55,
        95, 60, 58, 62, 65,
        68, 70, 97, 72, 75,
        78, 80, 85, 92, 88
    ],

    "Memory": [
        60, 62, 61, 63, 64,
        65, 66, 65, 67, 68,
        69, 70, 71, 72, 73,
        74, 75, 76, 77, 78
    ],

    "Response_Time": [
        120, 125, 130, 128, 135,
        140, 145, 150, 155, 160,
        165, 170, 175, 180, 185,
        190, 195, 200, 205, 210
    ]
}

df = pd.DataFrame(data)

# 2. Basic statistics
print("Basic Statistics:")
print(df[["CPU", "Memory", "Response_Time"]].describe())

# 3. Detect anomalies using threshold
CPU_THRESHOLD = 90

df["Anomaly"] = df["CPU"] > CPU_THRESHOLD

# 4. Print anomaly records
anomalies = df[df["Anomaly"] == True]

print("\nTotal records:", len(df))
print("Anomalies detected:", len(anomalies))

print("\nAnomalous Records:")
print(anomalies[["Timestamp", "CPU", "Anomaly"]])

# 5. Display graph
plt.figure(figsize=(10, 5))

plt.plot(df["Timestamp"], df["CPU"], marker="o", label="CPU Usage")

# Plot anomalies
plt.scatter(
    anomalies["Timestamp"],
    anomalies["CPU"],
    color="red",
    s=100,
    label="Anomaly"
)

plt.axhline(
    y=CPU_THRESHOLD,
    color="orange",
    linestyle="--",
    label="Threshold"
)

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps CPU Anomaly Detection")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()



# in short
# plt.plot(df["Timestamp"], df["CPU"])
# plt.scatter(anomalies["Timestamp"], anomalies["CPU"])
# plt.axhline(threshold)
# plt.show()