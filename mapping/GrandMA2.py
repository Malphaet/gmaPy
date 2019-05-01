class BasicMessageParse(object):
    """Classic System Specific Midi Message as Hex (BasicSyHexParse).
    Uses one method, parseMidi to parse the message and return a BasicMapping object with the mapping of the message inside"""

    def __init__(self):
        '''Basic init'''
        self.mapping={"value":None,"type":None} # A barebone initialisation, unusable, it will need to be overridden to work
        self.value=None
        self.

    def parseMidi(self,message):
        """Take a midi SyxEx message and return a BasicMapping"""
        pass

class BasicMapping(object):
    """A basic reading of the message, propreties are initialised depending on the way the SyEx message is formed,
    this objet will need the configuration to read and understand the message
    """
    def __init__(self):
        pass
