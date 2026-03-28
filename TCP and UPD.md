**What is TCP?**

TCP = Transmission Control Protocol
**Meaning**
TCP is a connection-oriented protocol.
That means before sending data, it establishes a connection between sender and receiver.
# Purpose

*Reliable data transfer*
Ensures:
Data arrives in order
No data is lost
No duplicates

**How it works**
Uses a 3-way handshake (connect → confirm → start)
Uses acknowledgments (ACKs)
Retransmits lost packets

**Used for:**
Web browsing → HTTP/HTTPS
Emails → SMTP
File transfer → FTP
Secure connections → SSH

**Common TCP Ports**
20/21 → FTP
22 → SSH
25 → SMTP
80 → HTTP
443 → HTTPS

**What is UDP?**
UDP = User Datagram Protocol

**Meaning
UDP is a connectionless protocol.
It sends data without setting up a connection first.

**Purpose**
Fast data transmission
No delay for checking errors or order

**How it works**
Just sends packets (called datagrams)
No:
Acknowledgment
Error correction
Ordering

**Used for:
Streaming (YouTube, Netflix)
Online gaming
Voice/video calls (VoIP)
DNS queries
# Common UDP Ports
53 → DNS
67/68 → DHCP
69 → TFTP
123 → NTP

**TCP vs UDP (Quick Comparison)**
*Feature TCP & UDP 
Connection Yes No
Reliability High Low
Speed Slower Faster
Order Guaranteed Not guaranteed
Use case Important data Real-time data
## CONCLUSION
TCP = Careful & Reliable (like sending a registered mail)
UDP = Fast & careless (like shouting a message)

**TCP ports are often targeted for:**
Port scanning
Exploits (e.g., port 80, 443)

**UDP ports are used in:**
DDoS attacks (because no handshake)
DNS amplification attacks
