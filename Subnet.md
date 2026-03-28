## What is a Subnet?
A subnet (subnetwork) is a smaller division of a large network.
Instead of one big network, we split it into smaller networks called subnets.
Example:
One network → 192.168.1.0
You divide it → multiple smaller networks like:
192.168.1.0
192.168.1.64
192.168.1.128
192.168.1.192
## Purpose of Subnetting
Subnetting is done for these main reasons:
# 1. Security
Separate departments (e.g., students vs teachers)
Prevent unauthorized access
# 2. Better Performance
Smaller networks = less traffic
Faster communication
# 3. Efficient IP Usage
Avoid wasting IP addresses
Assign only what is needed
# 4.  Easier Management
Easier to troubleshoot problems
Easier to control network
 Key Concepts You MUST Know
# 5. IP Address
Example:

192.168.1.10
2. Subnet Mask
Example:

255.255.255.0
This tells us:
Which part is network
Which part is host
 How to Calculate Subnet (Step-by-Step)
Step 1: Convert Subnet Mask to Binary
Example:

255.255.255.0
Binary:

11111111.11111111.11111111.00000000
 Count the 1s → this is called CIDR notation

= /24
Step 2: Find Number of Hosts
## Formula:

**Hosts = 2^n - 2**
Where:
n = number of 0s in subnet mask
**Example:
/24 → 8 zeros

**Hosts = 2^8 - 2 = 256 - 2 = 254 hosts
Step 3: Find Number of Subnets
Formula:

**Subnets = 2^borrowed bits
Example: If original was /16 and now /24:
Borrowed = 8 bits

**Subnets = 2^8 = 256 subnets
Step 4: Find Subnet Range (Important)
Example: Subnet mask:

255.255.255.192
**Binary last octet:

192 = 11000000
 ## block size:

256 - 192 = 64
So subnets are:

**192.168.1.0
192.168.1.64
192.168.1.128
192.168.1.192

**Step 5: Identify Network, Host, Broadcast**
Example: 192.168.1.64 /26
Network: 192.168.1.64
First host: 192.168.1.65
Last host: 192.168.1.126
Broadcast: 192.168.1.127
## Summary
Subnet = smaller network inside a big network
Purpose = security, performance, efficient IP usage
**Key formulas:
Hosts = 2ⁿ − 2
Subnets = 2^borrowed bits
Block size = 256 − subnet value