from scapy.all import *
from threading import Thread
from time import sleep
import Hook
from scapy.layers.inet import IP
from scapy.layers.inet import ICMP
from scapy.layers.inet import TCP
from scapy.all import DNS, DNSQR, sr1, UDP

class NTPSScapy(Thread):

    interface = ""
    
    def  __init__(self, interface="eth0"):
        super().__init__()

        self.interface = interface

    def run(self):
        sniff(iface=self.interface, prn=self.dissectPacket)
    
    def dissectPacket(self, packet):
        """ Dissects a packet using scapy and converts the data into a dictionary for easier manipulation."""
        #payload = packet.command()
        # packetDict = {}
        # packetDict["commandStr"] = payload 
        # packetDict["drop"] = False
        # packetDict["forward"] = False
        # payload = payload.replace("\'", "")
        # print("\n\n\n" + payload)
        # layerSplit = payload.split("/")
        # currentLayer = ""
        # layerFields = ""
        # fields = ""
        # fieldValuePair = ""
        # for i in range(0,len(layerSplit)):
        #     layerSplit[i] = layerSplit[i].replace(")", "")
        #     layerFields = layerSplit[i].split("(")
        #     currentLayer = layerFields[0]
        #     packetDict[currentLayer] = {}
        #     if currentLayer != "Raw":
        #         fields = layerFields[1].split(",")
        #         for j in range(0, len(fields)):
        #             fieldValuePair = fields[j].split("=")
        #             self.printList(fieldValuePair)
        #             if len(fieldValuePair) == 1:
        #                 pass
        #             elif len(fieldValuePair) == 2:
        #                 packetDict[currentLayer][fieldValuePair[0].strip()] = fieldValuePair[1]
        #             else:
        #                 actualString = ""
        #                 for i in range (1, len(fieldValuePair)):
        #                     if i == 1: 
        #                         actualString = fieldValuePair[i]
        #                     else: 
        #                         actualString = actualString + "=" + fieldValuePair[i]
        #                 packetDict[currentLayer][fieldValuePair[0].strip()] = actualString
        #     else: 
        #         packetDict[currentLayer] = layerFields[1]
        
        # for keys,values in packetDict.items():
        #     print(keys)
        #     print(values)



        hk = Hook.Hook("/root/Documents/SoftwareEngineeringII/TestHooks/testHook.py", "Test Hook", "Hook used to accomplish test cases.")
        hk.runHook(packet)




        

    def printList(self, l):
        for i in range(0, len(l)):
            print(l[i])




sniffer = NTPSScapy()

print("[***** Start sniffing *****]")
sniffer.start()

try:
    while True:
        sleep(100)
except KeyboardInterrupt:
    print("[***** Stop sniffing *****]")
    sniffer.join()
    
