import scapy.all as sc


def scan(ip: str):
    arp_req = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    print(broadcast.summary())
    # create a new packet combining the previous ones
    arp_req_broadcast = broadcast / arp_req
    arp_req_broadcast.show()

if __name__ == "__main__":
    ip = "127.0.0.0/300"
    scan(ip)
