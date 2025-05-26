from sklearn.ensemble import IsolationForest
import pandas as pd
from feature_extraction import extract_features
from alert_system import alert  # Uses winsound

def detect_anomalies(log_file='dns_log.csv'):
    full_df = pd.read_csv(log_file)
    features = extract_features(log_file)

    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(features)

    preds = model.predict(features)

    anomalies = full_df[preds == -1]
    print("🔍 Anomalous Queries Detected:")
    print(anomalies)

    if not anomalies.empty:
        alert()

if __name__ == "__main__":
    detect_anomalies()
