from charm.core.math.pairing import G1
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand


def generate_a(identity):
    return group.hash(identity, G1)


def generate_random():
    scr = OpenSSLRand()
    return int.from_bytes(scr.getRandomBytes(32), byteorder='big')


def get_x():
    return x


def generate_u(identity):
    return x * generate_a(identity)


def generate_v(identity, alpha, y_server, s):
    return -(x + y_server) * ((s * generate_a(identity)) + (alpha * generate_a(identity)))


group = PairingGroup('BN256')
x = generate_random()
