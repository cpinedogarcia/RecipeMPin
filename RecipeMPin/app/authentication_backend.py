from django.contrib.auth.models import User


class AuthenticationBackend(object):
    def authenticate(self, username, password):
        return User.objects.get(username='carlos')
        # ta = TrustedAuthority(pin)
        # x, y, secret = get_x(), get_y(), ta.get_secret()
        # u = generate_u(username)
        # v = generate_v(username, pin, y, secret)
        # result = magic_happens(username, v, u, ta)
        # if str(result) == '[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]':
        #     print('ok')
        #     return True
        #     # with open('failed.txt', 'w+') as file_:
        #     #     file_.write('ok')
        # else:
        #     print('rejected')
        #     return None
        #     # with open('failed.txt', 'w+') as file_:
        #     #     file_.write('rejected')

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
