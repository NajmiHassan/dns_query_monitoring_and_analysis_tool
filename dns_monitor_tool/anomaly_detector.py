# anomaly_detector.py
from sklearn.ensemble import IsolationForest
import pandas as pd
from feature_extraction import extract_features
from alert_system import alert
import os
import glob

def detect_anomalies(log_file=None):
    # If no file specified, find the most recent DNS queries file
    if log_file is None:
        csv_files = glob.glob('dns_queries_20250531_202452.csv')
        if not csv_files:
            print(" No DNS query CSV files found!")
            return
        log_file = max(csv_files, key=os.path.getctime)  # Get most recent file
        print(f" Using file: {log_file}")
    
    try:
        # Read the full dataset
        full_df = pd.read_csv(log_file)
        print(f" Loaded {len(full_df)} DNS queries")
        
        # Extract features
        features = extract_features(log_file)
        
        # Check if we have enough data for anomaly detection
        if len(features) < 10:
            print("⚠️  Not enough data for reliable anomaly detection (need at least 10 queries)")
            return
        
        # Train Isolation Forest model
        # Adjust contamination based on dataset size
        contamination_rate = min(0.1, max(0.01, 5/len(features)))  # Between 1% and 10%
        model = IsolationForest(contamination=contamination_rate, random_state=42, n_estimators=100)
        model.fit(features)
        
        # Predict anomalies
        preds = model.predict(features)
        anomaly_indices = preds == -1
        
        # Get anomalous queries
        anomalies = full_df[anomaly_indices].copy()
        
        print(f"\n Anomaly Detection Results:")
        print(f"   Total queries analyzed: {len(full_df)}")
        print(f"   Anomalies detected: {len(anomalies)}")
        print(f"   Contamination rate: {contamination_rate:.2%}")
        
        if not anomalies.empty:
            print(f"\n Anomalous DNS Queries:")
            print("=" * 60)
            for idx, row in anomalies.iterrows():
                print(f"⚠️  {row['Timestamp']} | {row['Query']}")
            
            # Save anomalies to file
            anomaly_file = f"anomalies_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
            anomalies.to_csv(anomaly_file, index=False)
            print(f"\n Anomalies saved to: {anomaly_file}")
            
            # Trigger alert
            alert()
        else:
            print(" No anomalous DNS activity detected.")
            
    except FileNotFoundError:
        print(f" File not found: {log_file}")
    except Exception as e:
        print(f" Error during anomaly detection: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    detect_anomalies()
