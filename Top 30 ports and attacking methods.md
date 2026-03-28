<pre>
Port 20 – FTP (data transfer)
Port 21 – FTP (control/commands)
Port 22 – SSH (secure remote login)
Port 23 – Telnet (insecure remote login)
Port 25 – SMTP (sending emails)
Port 53 – DNS (domain name resolution)
Port 67 – DHCP (server assigns IP addresses)
Port 68 – DHCP (client receives IP)
Port 69 – TFTP (simple file transfer)
Port 80 – HTTP (web browsing)
Port 110 – POP3 (email retrieval)
Port 119 – NNTP (news groups)
Port 123 – NTP (time synchronization)
Port 137 – NetBIOS (name services)
Port 138 – NetBIOS (datagram service)
Port 139 – NetBIOS (session service)
Port 143 – IMAP (email access)
Port 161 – SNMP (network management)
Port 179 – BGP (routing between networks)
Port 389 – LDAP (directory services)
Port 443 – HTTPS (secure web browsing)
Port 445 – SMB (file sharing, Windows)
Port 465 – SMTPS (secure email sending)
Port 500 – ISAKMP (VPN setup)
Port 514 – Syslog (system logging)
Port 515 – LPD (printer service)
Port 520 – RIP (routing protocol)
Port 587 – SMTP (secure mail submission)
Port 993 – IMAPS (secure email access)
Port 3389 – RDP (remote desktop access)
</pre>
## How Attackers Target Ports (Concept Only)
Instead of “how to attack,” here’s how attacks generally happen:
**1. Port Scanning**
Attackers check which ports are open using tools (like scanners)
Open port = possible entry point
**Defense:**
Close unused ports
Use firewalls
**2. Brute Force Login Attacks**
Common on:
Port 22 (SSH)
Port 3389 (RDP)
**Defense:**
Strong passwords
Limit login attempts
Use 2FA
**3. Exploiting Vulnerabilities**
Example:
Port 445 (SMB) → exploited by ransomware (like WannaCry)
**Defense:**
Keep systems updated (patching)
Disable old protocols (SMBv1)
**4. Man-in-the-Middle / Sniffing**
Happens on insecure ports like:
Port 21 (FTP)
Port 23 (Telnet)
**Defense**:
Use encrypted alternatives:
SSH instead of Telnet
HTTPS instead of HTTP
5. Reflection / DDoS Attacks
Uses UDP ports like:
53 (DNS)
123 (NTP)
**Defense**:
Disable open public access
Rate limiting

