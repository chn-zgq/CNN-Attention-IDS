from scapy.all import *
from scapy.layers.inet import TCP, UDP
from scapy.layers.l2 import Ether

pcap_feature = {
    "mac_src": None,
    "mac_dst": None,
    "src_port": None,
    "dst_port": None,
    "type": None
}


def sniffer():
    pkts = sniff(filter="tcp or udp or icmp", count=1000, prn=lambda x: print(x))
    wrpcap("./Data/Pcap/sniffer.pcap", pkts)


def get_pcap_data():
    pkts = rdpcap("./Data/Pcap/sniffer.pcap")
    pcap_list = []
    for pkt in pkts:
        if pkt.haslayer(Ether):
            pcap_feature["mac_src"] = pkt[Ether].src
            pcap_feature["mac_dst"] = pkt[Ether].dst
        if pkt.haslayer(IP):
            pcap_feature["type"] = pkt[IP].proto
        if pkt.haslayer(TCP):
            pcap_feature["src_port"] = pkt[TCP].sport
            pcap_feature["dst_port"] = pkt[TCP].dport
        if pkt.haslayer(UDP):
            pcap_feature["src_port"] = pkt[UDP].sport
            pcap_feature["dst_port"] = pkt[UDP].dport
        pcap_list.append(list(pcap_feature.values()))
    return pcap_list
