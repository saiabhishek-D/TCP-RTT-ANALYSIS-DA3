DA3 - TCP Round Trip Time Analysis using Wireshark and hping3
Name: Sai Abhishek D
Reg No: 24BCE1619
Department: SCOPE, VIT Chennai
Course: Computer Networks
Semester: Winter Semester, B.Tech CSE (2024–2025)

Overview
This repository contains all code, pcap files, graphs, and resources for DA3 of the Computer Networks Lab assignment on TCP Round Trip Time Analysis. RTT behavior was studied across six traffic conditions — Normal, Low, Medium, Heavy WiFi, Heavy Hotspot, and Duplicate ACK — using Wireshark for packet capture, hping3 for controlled traffic generation, and a custom Scapy script for RTT extraction and visualization.

Objective
To capture, measure, and analyze Round Trip Time (RTT) and Jitter under six distinct traffic conditions using hping3 on Ubuntu Linux and Wireshark, and visualize the results programmatically using Python and Scapy.

Tools Used

Python 3 + Scapy
hping3
Wireshark
matplotlib
numpy
Ubuntu Linux


Files
FileDescriptionrtt_analysis.pyMain Scapy script — reads pcapng files and plots RTT vs Time, RTT vs Throughput, RTT vs Packet Ratecomparison.pyPlots Average RTT and Jitter comparison bar charts across all six traffic conditionsnormal_capture.pcapngWireshark capture — Normal traffic (passive, no injection)low_capture.pcapngWireshark capture — Low traffic (100 pps)medium_capture.pcapngWireshark capture — Medium traffic (200 pps)heavy_wifi.pcapngWireshark capture — Heavy traffic on WiFi (1000 pps)heavy_hotspot.pcapngWireshark capture — Heavy traffic on Mobile Hotspot (1000 pps)dup_ack_capture.pcapngWireshark capture — Duplicate ACK trafficgraphs/Folder containing all 20 exported graph screenshotsscreenshots/Folder containing all Wireshark capture screenshots

Commands Used
Low Traffic
bashsudo hping3 1.1.1.1 -S -p 443 -i u10000 -d 256
Medium Traffic
bashsudo hping3 1.1.1.1 -S -p 443 -i u5000 -d 512
Heavy Traffic
bashsudo hping3 1.1.1.1 -S -p 443 -i u1000 -c 1000
Duplicate ACK Traffic
bashsudo hping3 1.1.1.1 -S -p 443 -i u50000 -c 100 --tcp-timestamp

Results Summary
ConditionAvg RTTJitterSamplesNormal195.85 ms104.17 ms23Low15.65 ms10.92 ms31Medium53.71 ms23.11 ms26Heavy WiFi1435.89 ms33.65 ms3493Heavy Hotspot1962.86 ms13.92 ms10906Duplicate ACK1560.44 ms2813.91 ms12

Blog Link
[Insert your Blogger link here]

Video Link
[Insert your YouTube link here]

References

SharkFest sessions and TCP analysis tutorials
Video reference: https://youtu.be/Tz6IfyfodKo?si=TrkgeYumh8Ix5cN3
Wireshark TCP Stream Graphs docs: https://www.wireshark.org/docs/wsug_html_chunked/ChStatTCPStreamGraphs.html
hping3 manual: http://www.hping.org/manpage.html
RFC 6298 — TCP Retransmission Timer: https://datatracker.ietf.org/doc/html/rfc6298
GeeksforGeeks RTT: https://www.geeksforgeeks.org/round-trip-time-rtt/


Just fill in your name, reg number, semester, blog link, and YouTube link and this is ready to push to GitHub!
