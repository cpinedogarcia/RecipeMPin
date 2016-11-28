from charm.core.math.pairing import G1
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand


class Client():
    def __init__(self, identity, alpha):
        self.group = PairingGroup('BN256')
        self.x = self.generate_random()
        self.identity = identity
        self.alpha = alpha
        self.a = self.generate_a()

    def generate_a(self):
        return self.group.hash(self.identity, G1)

    def generate_random(self):
        scr = OpenSSLRand()
        return int.from_bytes(scr.getRandomBytes(32), byteorder='big')

    def get_x(self):
        return self.x

    def generate_u(self):
        return self.x * self.a

    def generate_v(self, y_server, s):
        return -(self.x + y_server) * ((s * self.a) + (self.alpha * self.a))
        # return -(x + y_server) * (((s - alpha) * a) + (alpha * a))
