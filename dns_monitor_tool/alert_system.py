import winsound

def alert():
    print("[ALERT] Anomalous DNS activity detected!")
    duration = 1000  # milliseconds
    freq = 1000  # Hz
    winsound.Beep(freq, duration)

from alert_system import alert
# Example: define anomalies as an empty list or DataFrame before using it
anomalies = []  # or use: import pandas as pd; anomalies = pd.DataFrame()

# ...
if anomalies:  # checks if the list is not empty; for DataFrame use: if not anomalies.empty:
    alert()