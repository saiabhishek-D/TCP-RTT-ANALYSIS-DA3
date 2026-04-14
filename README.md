# DA3 — TCP Round Trip Time Analysis using Wireshark and hping3

| | |
|---|---|
| **Name** | Sai Abhishek D |
| **Reg No** | 24BCE1619 |
| **Department** | SCOPE, VIT Chennai |
| **Course** | Computer Networks |
| **Semester** | Winter Semester, B.Tech CSE (2025–2026) |

---

## Overview

This repository contains all code, pcap files, graphs, and resources for DA3 of the Computer Networks Lab assignment on TCP Round Trip Time Analysis. RTT behavior was studied across six traffic conditions — Normal, Low, Medium, Heavy WiFi, Heavy Hotspot, and Duplicate ACK — using Wireshark for packet capture, hping3 for controlled traffic generation, and a custom Scapy script for RTT extraction and visualization.

---

## Objective

To capture, measure, and analyze Round Trip Time (RTT) and Jitter under six distinct traffic conditions using hping3 on Ubuntu Linux and Wireshark, and visualize the results programmatically using Python and Scapy.

---

## Tools Used

- Python 3 + Scapy
- hping3
- Wireshark
- matplotlib
- numpy
- Ubuntu Linux

---

## RTT Analysis Script

The file `rtt_tcp_analysis.py` contains the complete Python script used for RTT extraction and graph generation in this DA.

**To run the script:**

```bash
# Step 1 — Install dependencies
pip install scapy matplotlib numpy

# Step 2 — Edit the pcap filename inside the script
PCAP_FILE = "your_capture_file.pcapng"

# Step 3 — Run
python3 rtt_tcp_analysis.py
```

The script reads any `.pcapng` file captured using Wireshark, calculates RTT by matching TCP sequence numbers with ACK responses, and generates three graphs — RTT vs Time, RTT vs Throughput, and RTT vs Packet Rate.

> See `rtt_tcp_analysis.py` for the full code and `RTT_ANALYSIS.md` for detailed documentation.

---

## Files

| File | Description |
|---|---|
| `rtt_tcp_analysis.py` | Main Scapy script — reads pcapng files and plots RTT vs Time, RTT vs Throughput, RTT vs Packet Rate |
| `RTT_ANALYSIS.md` | Detailed documentation for the RTT analysis script |
| `comparison.py` | Plots Average RTT and Jitter comparison bar charts across all six traffic conditions |
| `PCAP_FILES.md` | Links to all pcapng capture files hosted on Google Drive |
| `graphs/` | Folder containing all 20 exported graph screenshots |
| `screenshots/` | Folder containing all Wireshark capture screenshots |

---

## Commands Used

**Normal Traffic**
```bash
# Passive capture only — no traffic injection
sudo wireshark
```
**Low Traffic**
```bash
sudo hping3 1.1.1.1 -S -p 443 -i u10000 -d 256
```
**Medium Traffic**
```bash
sudo hping3 1.1.1.1 -S -p 443 -i u5000 -d 512
```
**Heavy Traffic (WiFi and Mobile Hotspot)**
```bash
sudo hping3 1.1.1.1 -S -p 443 -i u1000 -c 1000
```
**Duplicate ACK Traffic**
```bash
sudo hping3 1.1.1.1 -S -p 443 -i u50000 -c 100 --tcp-timestamp
```

---

## Results Summary

| Condition | Avg RTT | Jitter | Samples |
|---|---|---|---|
| Normal | 195.85 ms | 104.17 ms | 23 |
| Low | 15.65 ms | 10.92 ms | 31 |
| Medium | 53.71 ms | 23.11 ms | 26 |
| Heavy WiFi | 1435.89 ms | 33.65 ms | 3493 |
| Heavy Hotspot | 1962.86 ms | 13.92 ms | 10906 |
| Duplicate ACK | 1560.44 ms | 2813.91 ms | 12 |

---

## Blog Link

> https://tcp-rtt-analysis-da3.blogspot.com/2026/04/tcp-rtt-analysis-under-various-traffic.html

## Video Link

> https://youtu.be/9tgw4o6n2AI

---

## References

- SharkFest sessions and TCP analysis tutorials
- Video reference: [https://youtu.be/Tz6IfyfodKo?si=TrkgeYumh8Ix5cN3](https://youtu.be/Tz6IfyfodKo?si=TrkgeYumh8Ix5cN3)
- Wireshark TCP Stream Graphs: [https://www.wireshark.org/docs/wsug_html_chunked/ChStatTCPStreamGraphs.html](https://www.wireshark.org/docs/wsug_html_chunked/ChStatTCPStreamGraphs.html)
- hping3 manual: [http://www.hping.org/manpage.html](http://www.hping.org/manpage.html)
- RFC 6298 — TCP Retransmission Timer: [https://datatracker.ietf.org/doc/html/rfc6298](https://datatracker.ietf.org/doc/html/rfc6298)
- GeeksforGeeks RTT: [https://www.geeksforgeeks.org/round-trip-time-rtt/](https://www.geeksforgeeks.org/round-trip-time-rtt/)

---

*DA3 — Computer Networks — SCOPE, VIT Chennai — Winter Semester 2024-2025*
