import hashlib
from random import SystemRandom

from RecipeMPin.app.client import Client
from RecipeMPin.app.server import Server
from RecipeMPin.app.trusted_authority import TrustedAuthority


def hash_identity(identity):
    hid = hashlib.sha256()
    hid.update(identity.encode('utf-8'))
    return hid.hexdigest()


def generate_random(q):
    return SystemRandom().randint(1, q)


def save_s(s):
    with open('failed.txt', 'w+') as file_:
        file_.write('%d' % s)


def test_pin():
    alpha = 1234
    identity = 'carlos.pinedo@cimat.mx'
    client = Client(identity, alpha)
    server = Server(identity)
    ta = TrustedAuthority(alpha)
    x, y, secret = client.get_x(), server.get_y(), ta.get_secret()
    u = client.generate_u()
    v = client.generate_v(y, secret)
    # save_s(s)
    result = server.magic_happens(v, u, ta)
    if str(result) == '[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]':
        print('ok')
    else:
        print('rejected')


test_pin()
