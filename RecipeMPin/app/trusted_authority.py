from charm.core.math.pairing import G2
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand

group = PairingGroup('BN256')
s = 0


def generate_random():
    scr = OpenSSLRand()
    return int.from_bytes(scr.getRandomBytes(49), byteorder='big')


def generate_s(pin):
    s = generate_random() + pin
    return s


def generate_q():
    return group.random(G2)


def generate_sq(s, q):
    return s * q
