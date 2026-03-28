In IP addressing (specifically IPv4 classes), Class D and Class E are very different from Classes A, B, and C. They are “special-purpose” classes, *not used for normal device-to-device communication.
# Class D (Multicast Addresses)
Range:
**224.0.0.0 → 239.255.255.255

What makes it special?
Class D is used for multicasting, not for assigning IPs to individual devices.
# What is Multicasting?
Instead of sending data to one device (unicast) or everyone (broadcast), multicast sends data to a specific group of devices.

**Example use:**
Live video streaming
Online gaming updates
Routing protocols (like OSPF)

 Example:
**224.0.0.1 → All hosts in a local network**

**Key characteristics:**
No network/host division
No subnetting
Devices join a multicast group to receive data
Efficient: saves bandwidth by sending one stream to many receivers

# *Class E (Experimental Addresses)

Range:
**240.0.0.0 → 255.255.255.254**
## What makes it special?
Class E is reserved for experimental and research purposes.

**Important notes:**
Not used in real-world networking
Most operating systems and routers block or ignore these addresses
Not assignable to devices

**Special case:**
255.255.255.255 → Limited broadcast address (used to send to all devices in a network)

**Key characteristics:**
Reserved by standards organizations
Used for testing new networking concepts
No practical use in normal networking today

# SHORTLY
D = Distribution (to groups)
E = Experiment

