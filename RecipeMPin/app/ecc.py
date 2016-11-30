import hashlib
from random import SystemRandom

from app.client import get_x, generate_u, generate_v
from app.server import get_y, magic_happens
from app.trusted_authority import TrustedAuthority


def hash_identity(identity):
    hid = hashlib.sha256()
    hid.update(identity.encode('utf-8'))
    return hid.hexdigest()


def generate_random(q):
    return SystemRandom().randint(1, q)


def save_s(s):
    with open('failed.txt', 'w+') as file_:
        file_.write('%d' % s)


# def test_pin():
#     alpha = 1234
#     identity = 'carlos.pinedo@cimat.mx'
#     client = Client(identity, alpha)
#     server = Server(identity)
#     ta = TrustedAuthority(alpha)
#     x, y, secret = client.get_x(), server.get_y(), ta.get_secret()
#     u = client.generate_u()
#     v = client.generate_v(y, secret)
#     result = server.magic_happens(v, u, ta)
#     if str(result) == '[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]':
#         print('ok')
#     else:
#         print('rejected')


def autenticate(alpha, identity, pin):
    ta = TrustedAuthority(pin)
    x, y, secret = get_x(), get_y(), ta.get_secret()
    with open('secret.txt', 'w+') as file_:
        file_.write(str(secret))
    u = generate_u(identity)
    v = generate_v(identity, alpha, y, secret)
    result = magic_happens(identity, v, u, ta)
    if str(result) == '[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]':
        print('ok')
        with open('failed.txt', 'w+') as file_:
            file_.write('ok')
        return True
    else:
        print('rejected')
        with open('failed.txt', 'w+') as file_:
            file_.write('rejected')
        return False
