import socket
from scapy.all import ARP, Ether, srp


def scan_ip(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(1)
            result = scanner.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port:5} | OPEN | Filtered  on {ip}")
            else:
                print(f"Port {port:5} | Closed")
                pass
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


if __name__ == "__main__":
    target_ip = input("Target Ip: ")

    arp_request = ARP(pdst=target_ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered_list = srp(packet, timeout=3, verbose=False)[0]

    if not answered_list:
        print("The IP is Down or not responding to ARP!!")
    else:
        received = answered_list[0][1]
        print(f"The Ip: {received.psrc}\nMac : {received.hwsrc} is Up!\n")

        cmn_ports = [
            21,
            22,
            23,
            53,
            80,
            123,
            443,
            1425,
            3306,
            3389,
            5426,
            5601,
            5985,
            1521,
            389,
            88,
        ]

        print("Starting Port Scan...")
        for port in cmn_ports:
            scan_ip(target_ip, port)
