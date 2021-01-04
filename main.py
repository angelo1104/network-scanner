import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=3)

    print('IP Address \t\t\t Mac Address \n-----------------------------------------------------')
    for answer in answered:
        print(f'{answer[1].psrc} \t\t\t {answer[1].hwsrc}')


scan('192.168.43.1/24')
