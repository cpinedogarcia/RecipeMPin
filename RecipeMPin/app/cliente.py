from charm.core.math.pairing import G1
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand

group = PairingGroup('BN256')


def generate_a(identity):
    return group.hash(identity, G1)


def generate_random():
    scr = OpenSSLRand()
    return int.from_bytes(scr.getRandomBytes(49), byteorder='big')


x = generate_random()


def get_x():
    return x


def generate_u(identity, x):
    return x * generate_a(identity)


def generate_v(y_server, identity, alpha, s, x):
    a = generate_a(identity)
    return (x + y_server) * (((s - alpha) * a) + (alpha * a))
    # return -(x + y_server) * (((s - alpha) * a) + (alpha * a))
