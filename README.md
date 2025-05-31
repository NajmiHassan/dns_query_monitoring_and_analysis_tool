<p align="center">
  <a href="https://youtu.be/rhLfQY4ghrY" target="_blank">
    <img src="https://img.youtube.com/vi/rhLfQY4ghrY/0.jpg" alt="Watch the video" />
  </a>
</p>

# DNS Query Monitoring and Analysis Tool

A Python-based tool for monitoring DNS queries on your network and detecting potentially malicious or suspicious domain name resolution patterns using machine learning.

## What This Tool Does

This tool captures and analyzes DNS queries happening on your network to identify unusual patterns that might indicate malicious activity like malware, botnets, or data exfiltration attempts. It uses machine learning to automatically detect anomalous DNS behavior and alerts you when suspicious activity is found.

## Features

- **Real-time DNS Monitoring**: Captures DNS queries as they happen on your network
- **Automatic Data Logging**: Saves all DNS queries to CSV files with timestamps
- **Machine Learning Detection**: Uses Isolation Forest algorithm to identify anomalous patterns
- **Feature Engineering**: Analyzes domain characteristics like length, structure, and suspicious patterns
- **Alert System**: Provides visual and audio alerts when threats are detected
- **Cross-platform Support**: Works on Windows, Linux, and macOS

## How It Works

1. **DNS Packet Capture**: The tool monitors network traffic for DNS queries (port 53)
2. **Data Collection**: All queries are logged with timestamps and domain names
3. **Feature Extraction**: Analyzes domain characteristics such as:
   - Domain name length
   - Number of subdomains
   - Presence of numbers or special characters
   - Unusual character patterns
4. **Anomaly Detection**: Machine learning model identifies queries that don't match normal patterns
5. **Alerting**: Suspicious activity triggers alerts and detailed reports

# Npcap Installation and Verification Guide

## 1. Install Npcap

**Download:** [Npcap Download Page](https://npcap.com/#download)

### During Installation:

- [x] Enable: "Install Npcap in WinPcap API-compatible Mode"
- [x] Enable: "Support raw 802.11 traffic" (optional)
- [x] Install as a service so it starts automatically

## 2. Verify Npcap Installation

After installation, open Command Prompt and type:

```bash
sc query npcap
```

It should show `RUNNING` status.

## 3. Restart Your Python Environment

Exit and re-enter your virtual environment (or restart terminal), just in case environment variables were affected.

## 4. Re-run Your DNS Sniffer Script

```bash
python dns_sniffer.py
```

If Npcap is installed correctly, this time it should begin live DNS traffic capture.

## Project Structure

```
dns_monitor_tool/
├── dns_sniffer.py          # Main DNS packet capture module
├── feature_extraction.py   # Domain feature analysis
├── anomaly_detector.py     # Machine learning detection engine
├── alert_system.py         # Alert and notification system
├── requirements.txt        # Python dependencies
└── README.md             
```

## Requirements

- Python 3.7 or higher
- Administrator/root privileges (required for packet capture)
- Network interface capable of packet sniffing

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/dns-monitoring-tool.git
   cd dns-monitoring-tool
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv dns_monitor_env
   source dns_monitor_env/bin/activate  # On Windows: dns_monitor_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

- `scapy` - Network packet manipulation and capture
- `pandas` - Data analysis and CSV handling
- `scikit-learn` - Machine learning algorithms
- `winsound` - Audio alerts (Windows only)

## Usage

### 1. Start DNS Monitoring

Run the DNS sniffer to begin capturing queries:

```bash
python dns_sniffer.py
```

**Note**: You must run this with administrator privileges:
- Windows: Run Command Prompt as Administrator
- Linux/macOS: Use `sudo python dns_sniffer.py`

Let it run for a while to collect DNS queries. Press `Ctrl+C` to stop and save the data.

### 2. Analyze for Anomalies

Once you have collected DNS data, run the anomaly detector:

```bash
python anomaly_detector.py
```

The tool will:
- Load the most recent DNS query log
- Extract features from domain names
- Train a machine learning model
- Identify and report suspicious queries
- Save anomalies to a separate file

### 3. Understanding Results

The tool outputs:
- **Total queries analyzed**: Number of DNS queries processed
- **Anomalies detected**: Number of suspicious queries found
- **Detailed anomaly list**: Timestamp and domain name of each suspicious query
- **Saved reports**: CSV files with anomalous queries for further investigation

## What Makes a DNS Query Suspicious?

The tool looks for patterns that might indicate malicious activity:

- **Unusually long domain names** (often used by malware)
- **High number of subdomains** (common in DGA - Domain Generation Algorithms)
- **Random-looking character patterns** (typical of automated malware)
- **Unusual character combinations** (numbers, hyphens in suspicious patterns)
- **Domains that don't match normal browsing patterns**

## Example Output

```
 Using file: dns_queries_20250531_182145.csv
 Loaded 156 DNS queries

 Anomaly Detection Results:
   Total queries analyzed: 156
   Anomalies detected: 3
   Contamination rate: 3.21%

 Anomalous DNS Queries:
============================================================
⚠️  2025-05-31 18:21:45 | xn--90a3ac.xn--90a3ac.example.com
⚠️  2025-05-31 18:22:12 | 8f4d2c1a9b7e.malicious-domain.net
⚠️  2025-05-31 18:22:34 | very-long-suspicious-domain-name-that-looks-automated.com

 Anomalies saved to: anomalies_20250531_182234.csv
```

## Configuration

You can modify the detection sensitivity by adjusting parameters in `anomaly_detector.py`:

- **Contamination rate**: Percentage of queries expected to be anomalous (default: 1-10%)
- **Minimum queries**: Minimum number of queries needed for analysis (default: 10)
- **Feature weights**: Importance of different domain characteristics

## Troubleshooting

### Common Issues

1. **Permission Denied**: Run with administrator/root privileges
2. **No packets captured**: Check if you're on the correct network interface
3. **No anomalies detected**: This is normal for clean networks; try collecting more data
4. **Import errors**: Ensure all dependencies are installed correctly

### Network Interface Issues

If you're not capturing packets, you might need to specify the network interface:

```python
# In dns_sniffer.py, modify the sniff function:
sniff(filter="udp port 53", prn=dns_callback, iface="eth0")  # Replace "eth0" with your interface
```

## Use Cases

- **Home Network Security**: Monitor family network for malware infections
- **Small Business Security**: Detect compromised devices on company network
- **Security Research**: Study DNS patterns and malware behavior
- **Network Forensics**: Investigate suspicious network activity
- **Educational Purposes**: Learn about DNS security and machine learning

## Limitations

- Requires network access and packet capture privileges
- May not detect all types of DNS-based threats
- Encrypted DNS (DoH/DoT) traffic cannot be monitored
- False positives may occur with legitimate but unusual domains
- Performance depends on network traffic volume

## Security Considerations

- This tool captures network traffic, so handle logs securely
- Be aware of privacy implications when monitoring shared networks
- Ensure compliance with local laws and regulations
- Use only on networks you own or have permission to monitor
