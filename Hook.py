import os
import importlib.util
import sys

class Hook:
    """ Class that stores the path to a hook that modifies packets."""
    path = ""
    name = ""
    desc = ""



    def __init__(self, path, hookName, description):
        """Takes in path and userfriendly name.If path is invalid, path variable is set to 'Invalid Path'""" 
        if self.validPath(path):
            self.path = path
        else:
            self.path = "Invalid Path"
        self.name = hookName
        self.desc = description
        
    def validPath(self, path):
        """ Checks for the existance of a path"""
        return os.path.exists

    def runHook(self, packet):
        """Runs the "editPacket" method from the hook found in the path. Packet is manipulated and passed by reference. To drop a packet, set packet reference to None. """
        directory, module_name = os.path.split(self.path)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, directory)
        try:
            module = __import__(module_name)
        finally:
            sys.path[:] = path 

        code = "module." + module_name + ".editPacket(packet)"
        exec(code)

    def getPath(self):
        """ Gets the path value."""
        return self.path

    def getName(self):
        """ Gets the name value."""
        return self.name

    def getDesc(self):
        """ Gets the description value."""
        return self.desc   

    def setPath(self, path):
        """ Sets the path value."""
        self.path = path

    def setName(self, name):
        """ Sets the name value."""
        self.name = name

    def setDesc(self, description):
        """ Sets the description value."""
        self.desc = description   