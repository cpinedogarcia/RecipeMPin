from charm.core.math.pairing import G1
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand


class Server():
    def __init__(self, identity):
        self.group = PairingGroup('BN256')
        self.y = self.generate_random()
        self.identity = identity
        self.a = self.generate_a()

    def generate_random(self):
        scr = OpenSSLRand()
        return int.from_bytes(scr.getRandomBytes(32), byteorder='big')

    def get_y(self):
        return self.y

    def generate_a(self):
        return self.group.hash(self.identity, G1)

    def magic_happens(self, v, u, ta):
        q = ta.get_q()
        sq = ta.generate_sq()
        return self.group.pair_prod(v, q) * self.group.pair_prod(u + (self.y * self.a), sq)
        # return group.pair_prod(generate_a(identity)*s, q) == group.pair_prod(generate_a(identity), sq)
        # return group.pair_prod(v / (u + (y * a)), q) == group.pair_prod((u + (y * a)) / v, sq)
