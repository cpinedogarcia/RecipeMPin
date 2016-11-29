from charm.core.math.pairing import G1
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand


def generate_random():
    scr = OpenSSLRand()
    return int.from_bytes(scr.getRandomBytes(32), byteorder='big')


def get_y():
    return y


def generate_a(identity):
    return group.hash(identity, G1)


def magic_happens(identity, v, u, ta):
    q = ta.get_q()
    sq = ta.generate_sq()
    return group.pair_prod(v, q) * group.pair_prod(u + (y * generate_a(identity)), sq)


group = PairingGroup('BN256')
y = generate_random()
