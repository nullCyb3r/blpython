from scapy.all import *

def tcp_sys_scan(target, ports):
    print(f"Scanning {target} for Open TCP ports....")
    
    for port in ports:
        src_port = RandShort()
        resp = sr1(IP(dst=target)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
        
        if resp is None:
            print(f"Port {port}: Filtered") 
        elif resp.haslayer(TCP):

            if resp.getlayer(TCP).flags == 0x12:
                sr(IP(dst=target)/TCP(sport=src_port, dport=port, flags="R"), timeout=1, verbose=0)
                print(f"Port {port}: Open")
            elif resp.getlayer(TCP).flags == 0x14:
                print(f"Port {port}: Closed")
        elif resp.haslayer(ICMP):
            if int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print(f"Port {port}: Filtered")

target = "192.168.10.1" 
ports = [21, 22, 23, 80, 443, 3389] 
tcp_sys_scan(target, ports)
