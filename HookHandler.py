import Hook
import HookCollection

class HookHandler:
    """Class that handles Hooks, Hook Collections, and PCAP functionality"""
    collections = []
    enabled = []


    def setHookName(self, collectionID, hookID, name):
        """Sets a hook's name"""
        self.collections[collectionID].getHook[hookID].setName(name)

    def setHookPath(self, collectionID, hookID, path):
        """Sets a hook's path"""
        self.collections[collectionID].getHook[hookID].setPath(path)

    def setHookDescription(self, collectionID, hookID, description)
        """Sets a hook's description"""
        self.collections[collectionID].getHook[hookID].setDesc(description)

    def setCollectionName(self, collectionID, name)
        """Sets the collection's name"""
        self.collections[collectionID].setName(name)

    def setCollectionStatus(self, collectionID, status)
        """Sets the Collection's status"""
        self.enabled[collectionID] = status

    def setHookInCollectionStatus(self, collectionID, hookID, status)
        """Enables or disables a hook within a collection """
        self.collections[collectionID].setHookStatus(hookID, status)

    def addHook(self, collectionID, hook)
        """Adds a hook to the collection """
        self.collections[collectionID].addHook(hook)

    def removeHook(self, collectionID, hookID)
        """Removes hook at an index within a collection"""
        self.collections[collectionID].removeHook(hookID)

    def setCollectionSequence(self, collectionID, hookSequence)
        """Reorders the sequence of hooks in a collection."""
        self.collections[collectionID].reorder(hookSequence)

    def removeCollection(self, collectionID):
        """Removes collection at an index. """
        newCollectionList = []
        newEnabledList = []
        i = 0
        j = 0
        while (i < len(self.collections))
            if j != collectionID:
                newCollectionList[i] = self.collections[j]
                newEnabledList[i] = self.enabled[j]
                i = i + 1
            j = j + 1
        self.collections = newCollectionList
        self.enabled = newEnabledList
    
    def reorder(self, sequence):
        """Reorders the execution order of collections in the overall collection. Passed a list of positional indexes"""
        newcollectionList = []
        newEnabledList = []
        for i in range(0, len(sequence)):
            newcollectionList[i] = self.collections[sequence[i]]
            newEnabledList[i] = self.enabled[sequence[i]]
        self.collections = newCollectionList
        self.enabled = newEnabledList

    def runCollections(self, packet):
        """ Calls run hook method for each collection in collection of collections if it is enabled."""
        for i in range(0, len(self.hooks)):
            if self.enabled[i]:
                self.collections[i].runCollection(packet)






        """Responsibility:Provide dictionary listing of information in packets in PCAP file
        Method Signature: def getPackets(pcapPath) 
        Pre-condition: /* @ require validPath(pcapPath) == true; */
        Post-Condition: /* @ ensures type(result) == dictionary; */"""

        """Responsibility:Add packet to PCAP file
        Method Signature: def getLayer(packetID, pcapPath) 
        Pre-condition: /* @ require validPacketID(packetID) == true; validPath(pcapPath) == true;*/
        Post-Condition: /* @ ensures type(result) == bool; */"""
