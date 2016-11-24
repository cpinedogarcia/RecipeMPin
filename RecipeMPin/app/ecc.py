import hashlib


def hash_identity(identity):
    hid = hashlib.sha256()
    hid.update(identity.encode('utf-8'))
    print(hid.hexdigest())
