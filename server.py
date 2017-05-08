from twisted.internet.protocol import Factory
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue
from mid_bullet import *


class FirstConnection(Protocol):
    def __init__(self, gs):
        self.gs = gs

    def connectionMade(self):
        data = dict()
        data['player1'] = self.gs.player1.pos
        data['player2'] = self.gs.player2.pos
        data['terrain'] = self.gs.terrain
        data['wind'] = self.gs.wind
        self.transport.write(data)

class BulletConnection(Protocol):
    def __init__(self, gs):
        self.gs = gs

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        assert len(data) == 2
        # create bullet locally
        self.gs.gameobjects.append(MidBullet.from_network(self, data[0], data[1]))

class TankConnection(Protocol):
    def __init__(self, gs):
        self.gs = gs

    def dataReceived(self, data):
        assert len(data) == 2
        pos = data[0]
        health = data[1]
        self.gs.player2.pos = pos
        self.gs.player2.health = health

class TerrainConnection(Protocol):
    def __init__(self, gs):
        self.gs = gs




class FirstFactory(Factory):
    def __init__(self, gs):
        self.myconn = FirstConnection(gs)

    def buildProtocol(self, addr):
        return self.myconn

class BulletFactory(Factory):
    def __init__(self, gs):
        self.myconn = BulletConnection(gs)

    def buildProtocol(self, addr):
        return self.myconn

class TankFactory(Factory):
    def __init__(self, gs):
        self.myconn = TankConnection(gs)

    def buildProtocol(self, addr):
        return self.myconn


class TerrainFactory(Factory):
    def __init__(self, gs):
        self.myconn = TerrainConnection(gs)

    def buildProtocol(self, addr):
        return self.myconn