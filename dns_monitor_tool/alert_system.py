# alert_system.py
import winsound
import sys
from datetime import datetime

def alert():
    """
    Trigger an alert when anomalous DNS activity is detected
    """
    try:
        print("\n" + "="*60)
        print(" [SECURITY ALERT] ")
        print("   Anomalous DNS activity detected!")
        print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        # Play alert sound on Windows
        if sys.platform == "win32":
            try:
                # Play multiple beeps to get attention
                for i in range(3):
                    winsound.Beep(1000, 500)  # 1000 Hz for 500ms
                    if i < 2:  # Don't sleep after the last beep
                        import time
                        time.sleep(0.2)
            except Exception as e:
                print(f"⚠️  Could not play alert sound: {e}")
        else:
            # For non-Windows systems, try system bell
            print("\a" * 3)  # System bell
            
        print(" Check the anomaly report for details.")
        
    except Exception as e:
        print(f" Error in alert system: {e}")

def log_alert(message):
    """
    Log alert to file for record keeping
    """
    try:
        with open("security_alerts.log", "a") as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"⚠️  Could not write to alert log: {e}")

if __name__ == "__main__":
    # Test the alert system
    alert()
