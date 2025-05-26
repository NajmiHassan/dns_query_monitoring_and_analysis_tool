# dns_logger.py
import csv
from datetime import datetime
from scapy.all import sniff, DNSQR, DNS

LOG_FILE = 'dns_log.csv'

def init_csv():
    with open(LOG_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'domain'])

def log_query(domain):
    with open(LOG_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), domain])

def dns_callback(packet):
    if packet.haslayer(DNSQR):
        domain = packet[DNSQR].qname.decode()
        print(f"[LOG] {domain}")
        log_query(domain)

def start_logging():
    init_csv()
    sniff(filter="udp port 53", prn=dns_callback, store=False)

if __name__ == "__main__":
    start_logging()
