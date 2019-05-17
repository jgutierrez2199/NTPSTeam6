import Hook

class HookCollection:
""" Collection of hooks that also tracks if the hooks are enabled or disabled."""
    name = ""
    hooks = []
    enabled = []

    def __init__(self, collectionName):
        """Sets up the Hook collection with its name."""
        self.name = collectionName

    def addHook(self, newHook):
        """Appends hook to end of collection."""
        if type(hook) == newHook:
            self.hooks.append(newHook)
            self.enabled[newHook.getName()] = True
        else: 
            pass
            
    def removeHook(self, hookNumber):
        """Removes Hook at an index. """
        del self.hooks[hookNumber]
        del self.enabled[hooknumber]
    
    def reorder(self, sequence):
        """Reorders the execution order of hooks in a collection. Passed a list of positional indexes"""
        newHookList = []
        newEnabledList = []
        for i in range(0, len(sequence)):
            newHookList[i] = self.hooks[sequence[i]]
            newEnabledList[i] = self.enabled[sequence[i]]
        self.hooks = newHookList
        self.enabled = newEnabledList

    def runCollection(self, packet):
        """ Calls run hook method for each hook in collection if it is enabled."""
        for i in range(0, len(self.hooks)):
            if self.enabled[i]:
                self.hooks[i].runHook(packet)
    
    def getName(self):
        """ Gets the name value."""
        return self.name

    def setName(self, name):
        """ Sets the name value."""
        self.name = name
        