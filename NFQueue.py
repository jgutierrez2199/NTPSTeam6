import scapy
import NTPSScapy
import netfilterqueue
import IPTables
import codecs

# def get_packet_layers(packet):
#     counter = 0
#     while True:
#         layer = packet.getlayer(counter)
#         if layer is None:
#             break

#         yield layer
#         counter += 1

# def print_and_accept(pkt):
#     print(pkt)
#     packet = Ether (pkt.get_payload())/IP (pkt.get_payload())/ ICMP (pkt.get_payload())
#     for layer in get_packet_layers(packet):
#         print (layer.name)
#         field_names = [field.name for field in layer.fields_desc]
#         fields = {field_name: getattr(layer, field_name) for field_name in field_names}
#         print (fields)
#     pkt.accept()

def packetsToDictionary(packet):
    Scapy.Scapy.dissect(packet)


tb = IPTables.IPTables()
tb.saveConfig()
tb.sendToNFQueue()

print(dir(netfilterqueue))

nfqueue = netfilterqueue()
nfqueue.bind(0, packetsToDictionary)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
tb.restoreConfig()