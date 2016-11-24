import hashlib
from random import SystemRandom


def hash_identity(identity):
    hid = hashlib.sha256()
    hid.update(identity.encode('utf-8'))
    return hid.hexdigest()


def generate_random(q):
    return SystemRandom().randint(1, q)
