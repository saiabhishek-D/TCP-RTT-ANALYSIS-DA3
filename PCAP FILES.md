# PCAP Files

Due to GitHub's 25MB file size limit, all pcap capture files are hosted on Google Drive.

## Download Link

[Click here to download all PCAP files](https://drive.google.com/drive/folders/1_ayXz0_4M309wH1DUfZ01_3ztFrbGV6B?usp=drive_link)

## Files Available

| File | Traffic Condition | Size |
|---|---|---|
| `G2_RTT_NORMAL.pcapng` | Normal — passive capture (Group 2) | 12 MB |
| `G2_RTT_MEDIUM.pcapng` | Medium — 200 pps (Group 2) | 133.8 MB |
| `G2_RTT_HEAVY.pcapng` | Heavy — WiFi 1000 pps (Group 2) | 8.3 MB |
| `G3_RTT_NORMAL.pcapng` | Normal — passive capture (Group 3) | 786 KB |
| `G3_RTT_HEAVY.pcapng` | Heavy — WiFi 1000 pps (Group 3) | 19.6 MB |
| `G3_RTT_VERY HEAVY.pcapng` | Heavy — Mobile Hotspot (Group 3) | 4.6 MB |
| `dup_ack.pcapng` | Duplicate ACK traffic | 58.6 MB |

## Note

- G2 = First round of captures (WiFi environment)
- G3 = Second round of captures (WiFi + Mobile Hotspot environment)
- All captures were done using Wireshark on Ubuntu Linux targeting 1.1.1.1 on port 443
- Files can be opened directly in Wireshark for analysis
- Total size: ~237 MB
