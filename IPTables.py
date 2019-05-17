import os 

class IPTables: 

    IPTableConfigFilePath = ""

    def __init__(self):
        self.IPTableConfigFilePath = "/etc/iptables.conf"

    def saveConfig(self):
        """save IPTable config"""
        os.system("iptables-save > " + self.IPTableConfigFilePath)
        

    def sendToNFQueue(self):
        """set IPTable rules to sned packets to NFQueue"""
        os.system("iptables -A INPUT -j NFQUEUE --queue-num 0")

    def restoreConfig(self):
        """save IPTable config"""
        os.system("iptables -P INPUT ACCEPT")
        os.system("iptables -P OUTPUT ACCEPT")
        os.system("iptables -P FORWARD ACCEPT")
        os.system("iptables -F")

