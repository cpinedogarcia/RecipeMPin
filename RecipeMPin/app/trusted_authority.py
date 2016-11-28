from charm.core.math.pairing import G2
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand


class TrustedAuthority():
    def __init__(self, alpha):
        self.group = PairingGroup('BN256')
        self.alpha = alpha
        self.s = self.generate_s()
        self.q = self.generate_q()

    def generate_random(self):
        scr = OpenSSLRand()
        return int.from_bytes(scr.getRandomBytes(32), byteorder='big')

    def generate_s(self):
        s = self.generate_random() + self.alpha
        return s

    def get_s(self):
        return self.s

    def generate_q(self):
        return self.group.random(G2)

    def get_q(self):
        return self.q

    def generate_sq(self):
        return self.s * self.q

    def get_secret(self):
        return self.s - self.alpha
