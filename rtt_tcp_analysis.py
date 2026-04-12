from scapy.all import rdpcap, TCP, IP
import matplotlib.pyplot as plt
import numpy as np

# ========== CONFIG ==========
PCAP_FILE = "ENTER THE PCAP FILE NAME IN PNG"   # <-- change this
WINDOW = 1.0                   # seconds
# ============================

packets = rdpcap(PCAP_FILE)

seq_time = {}          # seq tracking for RTT
rtt_list = []
rtt_time = []

throughput_bytes = {} # time_bin -> bytes
packet_count = {}     # time_bin -> packets

start_time = float(packets[0].time)

for pkt in packets:
    if pkt.haslayer(TCP) and pkt.haslayer(IP):
        tcp = pkt[TCP]
        ip = pkt[IP]

        pkt_time = float(pkt.time)
        rel_time = pkt_time - start_time
        bin_time = int(rel_time // WINDOW)

        # ---------- RTT ----------
        if len(tcp.payload) > 0:
            key = (ip.src, ip.dst, tcp.sport, tcp.dport, tcp.seq)
            seq_time[key] = pkt_time

        if tcp.flags & 0x10:  # ACK
            ack_key = (ip.dst, ip.src, tcp.dport, tcp.sport, tcp.ack - 1)
            if ack_key in seq_time:
                rtt = (pkt_time - seq_time[ack_key]) * 1000
                if rtt > 0:
                    rtt_list.append(float(rtt))
                    rtt_time.append(rel_time)
                del seq_time[ack_key]

        # ---------- Throughput ----------
        payload_len = len(tcp.payload)
        if payload_len > 0:
            throughput_bytes[bin_time] = throughput_bytes.get(bin_time, 0) + payload_len

        # ---------- Packet rate ----------
        packet_count[bin_time] = packet_count.get(bin_time, 0) + 1

# ---------- RTT STATS ----------
rtt_array = np.array(rtt_list, dtype=float)

if len(rtt_array) > 1:
    avg_rtt = np.mean(rtt_array)
    jitter = np.mean(np.abs(np.diff(rtt_array)))
else:
    avg_rtt = 0
    jitter = 0

# ---------- Throughput data ----------
tp = []
tp_time = []

for t in sorted(throughput_bytes):
    tp.append((throughput_bytes[t] * 8) / (WINDOW * 1_000_000))  # Mbps
    tp_time.append(t)

# ---------- Packet rate data ----------
pps = []
pps_time = []

for t in sorted(packet_count):
    pps.append(packet_count[t] / WINDOW)
    pps_time.append(t)

# ---------- ALIGN RTT WITH TP & PPS ----------
rtt_tp_x, rtt_tp_y = [], []
rtt_pps_x, rtt_pps_y = [], []

for i, rtt in enumerate(rtt_array):
    bin_t = int(rtt_time[i] // WINDOW)

    if bin_t < len(tp):
        rtt_tp_x.append(tp[bin_t])
        rtt_tp_y.append(rtt)

    if bin_t < len(pps):
        rtt_pps_x.append(pps[bin_t])
        rtt_pps_y.append(rtt)

# ---------- PLOTS ----------
plt.figure(figsize=(16, 4))

# 1️⃣ RTT vs Time
plt.subplot(1, 3, 1)
plt.plot(rtt_time, rtt_array, marker='o')
plt.xlabel("Time (s)")
plt.ylabel("RTT (ms)")
plt.title("RTT vs Time")
plt.grid(True)

plt.text(
    0.02, 0.95,
    f"Average RTT : {avg_rtt:.2f} ms\nJitter : {jitter:.2f} ms\nSamples : {len(rtt_array)}",
    transform=plt.gca().transAxes,
    verticalalignment="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
)

# 2️⃣ RTT vs Throughput
plt.subplot(1, 3, 2)
plt.scatter(rtt_tp_x, rtt_tp_y)
plt.xlabel("Throughput (Mbps)")
plt.ylabel("RTT (ms)")
plt.title("RTT vs Throughput")
plt.grid(True)

# 3️⃣ RTT vs Packet Rate
plt.subplot(1, 3, 3)
plt.scatter(rtt_pps_x, rtt_pps_y)
plt.xlabel("Packet Rate (pps)")
plt.ylabel("RTT (ms)")
plt.title("RTT vs Packet Rate")
plt.grid(True)

plt.tight_layout()
plt.show()
