# DA3 — TCP Round Trip Time Analysis using Wireshark and hping3

&nbsp;

| | |
|---|---|
| **Name** | Sai Abhishek D |
| **Reg No** | 24BCE1619 |
| **Department** | SCOPE, VIT Chennai |
| **Course** | Computer Networks |
| **Semester** | Winter Semester, B.Tech CSE (2024–2025) |

&nbsp;

---

&nbsp;

## Overview

&nbsp;

This repository contains all code, pcap files, graphs, and resources for DA3 of the Computer Networks Lab assignment on TCP Round Trip Time Analysis. RTT behavior was studied across six traffic conditions — Normal, Low, Medium, Heavy WiFi, Heavy Hotspot, and Duplicate ACK — using Wireshark for packet capture, hping3 for controlled traffic generation, and a custom Scapy script for RTT extraction and visualization.

&nbsp;

---

&nbsp;

## Objective

&nbsp;

To capture, measure, and analyze Round Trip Time (RTT) and Jitter under six distinct traffic conditions using hping3 on Ubuntu Linux and Wireshark, and visualize the results programmatically using Python and Scapy.

&nbsp;

---

&nbsp;

## Tools Used

&nbsp;

- Python 3 + Scapy
- hping3
- Wireshark
- matplotlib
- numpy
- Ubuntu Linux

&nbsp;

---

&nbsp;

## Files

&nbsp;

| File | Description |
|---|---|
| `rtt_analysis.py` | Main Scapy script — reads pcapng files and plots RTT vs Time, RTT vs Throughput, RTT vs Packet Rate |
| `comparison.py` | Plots Average RTT and Jitter comparison bar charts across all six traffic conditions |
| `normal_capture.pcapng` | Wireshark capture — Normal traffic (passive, no injection) |
| `low_capture.pcapng` | Wireshark capture — Low traffic (100 pps) |
| `medium_capture.pcapng` | Wireshark capture — Medium traffic (200 pps) |
| `heavy_wifi.pcapng` | Wireshark capture — Heavy traffic on WiFi (1000 pps) |
| `heavy_hotspot.pcapng` | Wireshark capture — Heavy traffic on Mobile Hotspot (1000 pps) |
| `dup_ack_capture.pcapng` | Wireshark capture — Duplicate ACK traffic |
| `graphs/` | Folder containing all 20 exported graph screenshots |
| `screenshots/` | Folder containing all Wireshark capture screenshots |

&nbsp;

---

&nbsp;

## Commands Used

&nbsp;

**Normal Traffic**
```bash
# Passive capture only — no traffic injection
sudo wireshark
```

&nbsp;

**Low Traffic**
```bash
sudo hping3 1.1.1.1 -S -p 443 -i u10000 -d 256
```

&nbsp;

**Medium Traffic**
```bash
sudo hping3 1.1.1.1 -S -p 443 -i u5000 -d 512
```

&nbsp;

**Heavy Traffic (WiFi and Mobile Hotspot)**
```bash
sudo hping3 1.1.1.1 -S -p 443 -i u1000 -c 1000
```

&nbsp;

**Duplicate ACK Traffic**
```bash
sudo hping3 1.1.1.1 -S -p 443 -i u50000 -c 100 --tcp-timestamp
```

&nbsp;

---

&nbsp;

## Results Summary

&nbsp;

| Condition | Avg RTT | Jitter | Samples |
|---|---|---|---|
| Normal | 195.85 ms | 104.17 ms | 23 |
| Low | 15.65 ms | 10.92 ms | 31 |
| Medium | 53.71 ms | 23.11 ms | 26 |
| Heavy WiFi | 1435.89 ms | 33.65 ms | 3493 |
| Heavy Hotspot | 1962.86 ms | 13.92 ms | 10906 |
| Duplicate ACK | 1560.44 ms | 2813.91 ms | 12 |

&nbsp;

---

&nbsp;

## Blog Link

&nbsp;

> [Insert your Blogger link here]

&nbsp;

---

&nbsp;

## Video Link

&nbsp;

> [Insert your YouTube link here]

&nbsp;

---

&nbsp;

## References

&nbsp;

- SharkFest sessions and TCP analysis tutorials
- Video reference: [https://youtu.be/Tz6IfyfodKo?si=TrkgeYumh8Ix5cN3](https://youtu.be/Tz6IfyfodKo?si=TrkgeYumh8Ix5cN3)
- Wireshark TCP Stream Graphs: [https://www.wireshark.org/docs/wsug_html_chunked/ChStatTCPStreamGraphs.html](https://www.wireshark.org/docs/wsug_html_chunked/ChStatTCPStreamGraphs.html)
- hping3 manual: [http://www.hping.org/manpage.html](http://www.hping.org/manpage.html)
- RFC 6298 — TCP Retransmission Timer: [https://datatracker.ietf.org/doc/html/rfc6298](https://datatracker.ietf.org/doc/html/rfc6298)
- GeeksforGeeks RTT: [https://www.geeksforgeeks.org/round-trip-time-rtt/](https://www.geeksforgeeks.org/round-trip-time-rtt/)

&nbsp;

---

&nbsp;

*DA3 — Computer Networks — SCOPE, VIT Chennai — Winter Semester 2024-2025*
