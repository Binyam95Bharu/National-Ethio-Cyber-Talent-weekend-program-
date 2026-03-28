
## 1. Physical Layer

### Common attacks:
- Cable tapping
- Device theft
- Signal jamming (Wi-Fi interference)
### How attackers do it:

- Physically access cables or hardware
- Use radio devices to **jam wireless signals**
- Interrupt communication by damaging infrastructure
 Example: Someone blocks Wi-Fi so your Telegram messages can’t send
## 2. Data Link Layer
### Common attacks:
- MAC spoofing
- ARP spoofing (Man-in-the-Middle)
### How attackers do it:

- Fake their **MAC address** to look like a trusted device
- Trick devices into sending data to them instead of the real router
 Result: attacker can **intercept or modify local network traffic**
## 3. Network Layer

### Common attacks:
- IP spoofing
- Packet sniffing
- Routing attacks
### How attackers do it:
- Forge IP addresses to hide identity
- Capture packets traveling across the network
- Manipulate routing paths to redirect traffic
 Example: Data meant for a server is secretly rerouted through attacker systems
## 4. Transport Layer

### Common attacks:
- TCP SYN flood (DoS attack)
- Session hijacking
### How attackers do it:
- Send fake connection requests to overwhelm a server
- Predict or steal session identifiers to take over a connection
 Result: services become slow or unavailable
## 5. Session Layer
### Common attacks:
- Session hijacking
- Replay attacks
### How attackers do it:
- Steal session tokens (e.g., login session IDs)
- Reuse captured communication to impersonate a user
 Example: Attacker takes over your logged-in Telegram session
## 6. Presentation Layer
### Common attacks:
- Encryption attacks
- Data manipulation
### How attackers do it:
- Exploit weak encryption or outdated protocols
- Try to decode or alter formatted data

 Result: sensitive data may be exposed
## 7. Application Layer

### Common attacks:
- Phishing
- Malware
- SQL injection
- Cross-site scripting (XSS)
### How attackers do it:
- Trick users into clicking malicious links
- Exploit software vulnerabilities
- Inject harmful input into applications
 Example: Fake Telegram login page steals your password.