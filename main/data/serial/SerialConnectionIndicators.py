class SerialConnectionIndicators():
    def __init__(self):
        self.isConnectionEstablished = False
        self.currConnectionID = None
        self.lastConnectionID = None

    def isConnected(self):
        return self.isConnectionEstablished

    def setCurrConnectionID(self, id):
        self.currConnectionID = id

    def getCurrConnectionID(self):
        return self.currConnectionID

    def setLastConnectionID(self, id):
        self.lastConnectionID = id

    def getLastConnectionID(self):
        return self.lastConnectionID

    def setConnection(self, connectionStatus):
        self.isConnectionEstablished = connectionStatus
