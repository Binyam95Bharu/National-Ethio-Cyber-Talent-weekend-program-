# Top 30 Common Network Ports and Their Vulnerabilities

## Introduction

In computer networking, **ports** are logical communication endpoints used by protocols like **Transmission Control Protocol (TCP)** and **User Datagram Protocol (UDP)**. Ports allow multiple services to run on the same device while keeping their traffic separated.

Each service listens on a specific **port number**, which helps computers determine which application should receive incoming data.

Understanding common ports is very important in **cybersecurity, penetration testing, and network administration** because attackers often target vulnerable services running on these ports.

---

# Top 30 Ports and Their Vulnerabilities

## 1. Port 20 – FTP Data
**Protocol:** TCP  
**Service:** File transfer data channel for FTP

**Vulnerabilities**
- Data transmitted without encryption
- Packet sniffing attacks
- FTP bounce attack

## 2. Port 21 – FTP Control
**Protocol:** TCP  
**Service:** FTP command and control channel

**Vulnerabilities**
- Anonymous login abuse
- Brute-force login attempts
- Credentials transmitted in plaintext

## 3. Port 22 – SSH
**Protocol:** TCP  
**Service:** Secure remote login using SSH

**Vulnerabilities**
- Password brute-force attacks
- Weak authentication
- Exploiting outdated SSH versions

## 4. Port 23 – Telnet
**Protocol:** TCP  
**Service:** Remote login via Telnet

**Vulnerabilities**
- No encryption
- Credentials visible in network traffic
- Man-in-the-Middle attacks

## 5. Port 25 – SMTP
**Protocol:** TCP  
**Service:** Email sending using SMTP

**Vulnerabilities**
- Email spoofing
- Open relay abuse
- Spam distribution

## 6. Port 53 – DNS
**Protocol:** TCP/UDP  
**Service:** Domain name resolution through DNS

**Vulnerabilities**
- DNS amplification attacks
- DNS cache poisoning
- DNS tunneling

## 7. Port 67 – DHCP Server
**Protocol:** UDP  
**Service:** IP address assignment using DHCP

**Vulnerabilities**
- Rogue DHCP servers
- DHCP starvation attacks

## 8. Port 68 – DHCP Client
**Protocol:** UDP

**Vulnerabilities**
- Man-in-the-Middle attacks
- IP spoofing

## 9. Port 69 – TFTP
**Protocol:** UDP  
**Service:** File transfer via TFTP

**Vulnerabilities**
- No authentication
- No encryption
- Unauthorized file access

## 10. Port 80 – HTTP
**Protocol:** TCP  
**Service:** Web communication via HTTP

**Vulnerabilities**
- Cross-Site Scripting (XSS)
- SQL injection
- Session hijacking

## 11. Port 110 – POP3
**Protocol:** TCP  
**Service:** Email retrieval using POP3

**Vulnerabilities**
- Credential sniffing
- Mailbox compromise

## 12. Port 119 – NNTP
**Protocol:** TCP  
**Service:** Network news service using NNTP

**Vulnerabilities**
- Information leakage
- Unauthorized access

## 13. Port 123 – NTP
**Protocol:** UDP  
**Service:** Time synchronization using NTP

**Vulnerabilities**
- Amplification attacks
- Reflection attacks

## 14. Port 137 – NetBIOS Name Service
**Protocol:** UDP  
**Service:** Name resolution using NetBIOS

**Vulnerabilities**
- Information disclosure
- Network enumeration

## 15. Port 138 – NetBIOS Datagram Service
**Protocol:** UDP

**Vulnerabilities**
- Network reconnaissance
- Packet spoofing

## 16. Port 139 – NetBIOS Session Service
**Protocol:** TCP

**Vulnerabilities**
- SMB attacks
- Null session enumeration

## 17. Port 143 – IMAP
**Protocol:** TCP  
**Service:** Email access via IMAP

**Vulnerabilities**
- Email interception
- Credential theft

## 18. Port 161 – SNMP
**Protocol:** UDP  
**Service:** Network monitoring using SNMP

**Vulnerabilities**
- Default community strings
- Device enumeration

## 19. Port 179 – BGP
**Protocol:** TCP  
**Service:** Internet routing via BGP

**Vulnerabilities**
- Route hijacking
- Traffic interception

## 20. Port 389 – LDAP
**Protocol:** TCP/UDP  
**Service:** Directory services using LDAP

**Vulnerabilities**
- LDAP injection
- Data leakage

## 21. Port 443 – HTTPS
**Protocol:** TCP  
**Service:** Secure web traffic using HTTPS

**Vulnerabilities**
- SSL/TLS misconfiguration
- Certificate attacks

## 22. Port 445 – SMB
**Protocol:** TCP  
**Service:** Windows file sharing via SMB

**Vulnerabilities**
- EternalBlue exploit
- Ransomware attacks like WannaCry

## 23. Port 465 – SMTPS
**Protocol:** TCP  
Secure email transmission

**Vulnerabilities**
- SSL misconfiguration
- Weak encryption

## 24. Port 500 – ISAKMP
**Protocol:** UDP  
Used in VPNs via ISAKMP

**Vulnerabilities**
- VPN brute force attacks
- Weak encryption algorithms

## 25. Port 514 – Syslog
**Protocol:** UDP  
Logging service using Syslog

**Vulnerabilities**
- Log injection
- Log tampering

## 26. Port 587 – SMTP Submission
**Protocol:** TCP

**Vulnerabilities**
- Credential brute force
- Spam abuse

## 27. Port 636 – LDAPS
**Protocol:** TCP  
Secure LDAP

**Vulnerabilities**
- Weak SSL configuration
- Certificate issues

## 28. Port 989 – FTPS Data
**Protocol:** TCP  
Secure FTP data transfer

**Vulnerabilities**
- Misconfigured encryption

## 29. Port 990 – FTPS Control
**Protocol:** TCP  
Secure FTP control channel

**Vulnerabilities**
- Weak authentication

## 30. Port 3389 – RDP
**Protocol:** TCP  
Remote desktop via RDP

**Vulnerabilities**
- Brute force login attempts
- BlueKeep vulnerability
- Remote access exploitation

---

# Summary Table

| Port | Service | Risk |
|-----|-----|-----|
| 21 | FTP | Plaintext credentials |
| 22 | SSH | Brute force |
| 23 | Telnet | No encryption |
| 53 | DNS | Amplification attack |
| 80 | HTTP | Web vulnerabilities |
| 445 | SMB | Worm attacks |
| 3389 | RDP | Remote exploitation |

---

# Useful Tool for Port Scanning

A popular port scanning tool is **Nmap**.

Example:

```bash
nmap -sV -p 1-1000 192.168.1.1
```

This command scans ports **1–1000** and detects running services.

