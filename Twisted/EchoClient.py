from twisted.internet import protocol, reactor
import datetime

class EchoClient(protocol.Protocol):

    def connectionMade(self):
        data = input('your message: ')
        self.transport.write(str.encode(data))
        #self.transport.write(str.encode(str(datetime.datetime.now()))
        #self.transport.write("Hello Twisted2")  #Unicode srting

    def dataReceived(self, data):
        if data == str.encode('quit'):
            self.transport.loseConnection()
        else:
            print("Server reply: ", str(data, 'utf-8'))
            self.connectionMade()
        #print("Server reply: ", data)
        #self.transport.loseConnection()

class EchoClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Fail to connect")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Lost connection")
        reactor.stop()



reactor.connectTCP("localhost", 8000, EchoClientFactory())
reactor.run()