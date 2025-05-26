# dns_sniffer.py
from scapy.all import sniff, DNSQR, DNS

def dns_callback(packet):
    if packet.haslayer(DNSQR):
        query = packet[DNSQR].qname.decode()
        print(f"[+] DNS Query: {query}")

def start_sniffing():
    sniff(filter="udp port 53", prn=dns_callback, store=False)

if __name__ == "__main__":
    print("Starting DNS sniffer...")
    start_sniffing()
