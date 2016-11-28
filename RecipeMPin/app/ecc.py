import hashlib
from random import SystemRandom

from RecipeMPin.app.cliente import get_x, generate_u, generate_v
from RecipeMPin.app.server import get_y, magic_happens
from RecipeMPin.app.trusted_authority import generate_s


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
    x, y, identity, s = get_x(), get_y(), 'carlos.pinedo@cimat.mx', generate_s(alpha)
    u = generate_u(identity, x)
    v = generate_v(y, identity, alpha, s, x)
    save_s(s)
    print(magic_happens(v, u, identity, s))


test_pin()
