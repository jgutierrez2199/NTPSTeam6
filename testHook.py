import re
from scapy.layers.inet import IP
from scapy.layers.inet import ICMP
from scapy.layers.inet import TCP
from scapy.all import DNS, DNSQR, sr1, UDP
from scapy.all import *
class testHook: 

    def editPacket(packet):
        """ This is the method that all Hooks need to have in order to edit packet data.""" 
        if "UDP" in packet.command():
            packet = packet[1]
            packet.sport =  44444
            packet[DNSQR].qname = "utep.edu"

            del packet.chksum
            packet.show2()
            send(packet) 
