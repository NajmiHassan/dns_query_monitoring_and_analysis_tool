import csv
import time
import os
import atexit
from scapy.all import sniff, DNSQR, DNS
from datetime import datetime

dns_queries = []

def dns_callback(packet):
    if packet.haslayer(DNSQR):
        query_name = packet[DNSQR].qname.decode("utf-8")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] DNS Query: {query_name}")
        dns_queries.append((timestamp, query_name))

def save_queries_to_csv():
    if dns_queries:
        filename = f"dns_queries_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Query"])
                writer.writerows(dns_queries)
            print(f"[*] DNS queries saved to {filename}")
            print(f"[*] Total {len(dns_queries)} queries captured")
        except Exception as e:
            print(f"[!] Failed to save DNS queries: {e}")
    else:
        print("[*] No DNS queries captured.")

def start_sniffing():
    # Test file writing permissions
    test_file = "test_output_check.txt"
    try:
        with open(test_file, "w") as f:
            f.write("File writing test.\n")
        print("[*] Successfully wrote test file.")
        os.remove(test_file)
        print("[*] Test file deleted.")
    except Exception as e:
        print(f"[!] Error handling test file: {e}")
        return

    print("Starting DNS sniffer... Press Ctrl+C to stop and save queries.")
    
    # Register the save function to run when program exits (even without Ctrl+C)
    atexit.register(save_queries_to_csv)

    try:
        # Add timeout parameter to prevent indefinite hanging
        sniff(filter="udp port 53", prn=dns_callback, store=False, timeout=300)  # 5 minutes timeout
        print("\n[*] Sniffing timeout reached. Saving queries...")
        save_queries_to_csv()
    except KeyboardInterrupt:
        print("\n[*] Stopping DNS sniffer due to keyboard interrupt...")
        save_queries_to_csv()
    except Exception as e:
        print(f"\n[!] Error during sniffing: {e}")
        save_queries_to_csv()

if __name__ == "__main__":
    start_sniffing()
