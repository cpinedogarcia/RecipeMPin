from charm.core.math.pairing import G2
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand

from RecipeMPin import settings


class TrustedAuthority():
    def __init__(self, alpha):
        self.group = PairingGroup('BN256')
        self.token = settings.TOKEN
        # self.token = self.generate_random()
        # with open('token.plain', 'r+') as file:
        #     file.seek(0)
        #     first_char = file.read(1)
        #     if not first_char:
        #         self.token = self.generate_random()
        #         file.write(self.token)
        #     else:
        #         file.seek(0)
        #         self.token = file.read()
        self.alpha = alpha
        self.s = self.generate_s()
        self.q = self.generate_q()
        # with open('q.plain', 'r+') as file:
        #     file.seek(0)
        #     first_char = file.read(1)
        #     if not first_char:
        #         file.write(self.q)
        #     else:
        #         file.seek(0)
        #         self.q = file.read()

    def generate_random(self):
        scr = OpenSSLRand()
        return int.from_bytes(scr.getRandomBytes(32), byteorder='big')

    def generate_s(self):
        s = self.token + self.alpha
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
        return self.token
