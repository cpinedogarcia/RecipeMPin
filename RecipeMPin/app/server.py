from charm.core.math.pairing import G1
from charm.toolbox.pairinggroup import PairingGroup
from charm.toolbox.securerandom import OpenSSLRand

from RecipeMPin.app.trusted_authority import generate_q, generate_sq

group = PairingGroup('BN256')


def generate_random():
    scr = OpenSSLRand()
    return int.from_bytes(scr.getRandomBytes(49), byteorder='big')


y = generate_random()


def get_y():
    return y


def generate_a(identity):
    return group.hash(identity, G1)


def magic_happens(v, u, identity, s):
    # s = get_s()
    y = get_y()
    q = generate_q()
    sq = generate_sq(s, q)
    a = generate_a(identity)
    return group.pair_prod(v, q) == group.pair_prod(u + (y * a), sq)
    # return group.pair_prod(generate_a(identity)*s, q) == group.pair_prod(generate_a(identity), sq)
    # return group.pair_prod(v / (u + (y * a)), q) == group.pair_prod((u + (y * a)) / v, sq)
