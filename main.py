from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
import time

connected_machines = []


def detect_connected_machines():
    global connected_machines
    ip_range = "192.168.1.0/24"  # Replace with your IP address range
    arp_request = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = ether / arp_request
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    for element in answered_list:
        machine = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        if machine not in connected_machines:
            print(f"{machine['ip']} | {machine['mac']} : \033[92mConnected\033[0m")
            connected_machines.append(machine)


if __name__ == "__main__":
    while True:
        print("\n--- Network Scan ---")
        detect_connected_machines()
        time.sleep(5)
