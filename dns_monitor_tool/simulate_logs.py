import csv
import random
from datetime import datetime, timedelta

# Simulated domain parts
subdomains = ['www', 'mail', 'ns1', 'ftp', 'cdn', 'auth']
domains = ['example', 'testsite', 'suspicious123', 'mybank', 'securedata', 'loginverify']
tlds = ['.com', '.net', '.org', '.xyz', '.ru', '.io']

def generate_random_domain():
    sub = random.choice(subdomains)
    domain = random.choice(domains)
    tld = random.choice(tlds)
    # Occasionally generate very suspicious domains
    if random.random() < 0.1:
        domain = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(20, 40)))
    return f"{sub}.{domain}{tld}"

def simulate_dns_logs(filename="dns_log.csv", n=500):
    start_time = datetime.now() - timedelta(minutes=n)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "domain"])
        for i in range(n):
            timestamp = (start_time + timedelta(seconds=i*5)).isoformat()
            domain = generate_random_domain()
            writer.writerow([timestamp, domain])
    print(f"[+] Simulated {n} DNS queries in {filename}")

if __name__ == "__main__":
    simulate_dns_logs()
