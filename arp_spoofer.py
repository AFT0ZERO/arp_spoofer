import optparse
import scapy.all as scapy
def get_argument():
    parser= optparse.OptionParser()
    parser.add_option('-t','--target',dest='target_ip' , help="Specify Vicitem IP Address")
    parser.add_option('-r','--router',dest='router_ip' , help="Specify Gatway IP Address")
    options, arguments=parser.parse_args()

    if not options.target_ip:
        parser.error('[-] Please Enter Target IP Address , -h for help.')
    
    if not options.router_ip:
        parser.error('[-] Please Enter Router IP Address , -h for help.')

    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = arp_broadcast/ arp_request
    answered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return answered[0][1].hwsrc

options = get_argument()
get_mac(options.target_ip)
