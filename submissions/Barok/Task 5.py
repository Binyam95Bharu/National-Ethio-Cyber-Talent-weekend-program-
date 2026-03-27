def classify_ip_address():
    address = input("Enter An Ip Address like 127.0.0.1/24......: ")
    if "/" not in address:
        print("Your Ip needs a subnetmask!!")
        return
    ip_address, subnet_mask = address.split("/")
    try:
        octets = [int(o) for o in ip_address.split(".")]
        if len(octets) != 4 or not all(0 <= o <= 255 for o in octets):
            print("Invalid Input!!")
            return
    except ValueError:
        print(
            "Plaese Use Proper Formatting for your Ip Address with numbers and dots(.)"
        )
        return
    first = octets[0]
    Ip_class = "Not in class A,B or C"
    if first < 128:
        Ip_class = "Class A"
    elif first < 192:
        Ip_class = "Class B"
    else:
        Ip_class = "Class C"
    is_private = False
    second = octets[1]

    if first == 10:
        is_private = True
    elif first == 172 and 16 <= second <= 31:
        is_private = True
    elif first == 192 and second == 168:
        is_private = True

    if first != 127:
        status = "Private" if is_private else "Public"
    else:
        status = "Loopback"

        ## Result
    print("Result :")
    print(f"Your Ip Address : {address}")
    print(f"Your Subnet Mask: {subnet_mask}")
    print(f"Your Class: {Ip_class}")
    print(f"Ip Status: {status}")


if __name__ == "__main__":
    classify_ip_address()
