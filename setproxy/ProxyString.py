

class ProxyString(object):
    """A proxy object"""
    def __init__(self, hostname, port, isHttps=True ):
        self.hostname = hostname
        self.port = port
        self.isHttps = isHttps
        self.protocol = "https" if isHttps else "http"
        self.username = None
        self.password = None

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def getProxyString(self):
        if self.username is not None:
            return "{}://{}:{}@{}:{}".format( self.protocol, self.username, self.password , self.hostname, self.port )
        else:
            return "{}://{}:{}".format( self.protocol, self.hostname, self.port )

    def __repr__(self):
        d = self.__dict__.copy()
        d["password"] = "*"*8;
        return str(d)