from django.contrib.auth.tokens import PasswordResetTokenGenerator


class MagicLinkTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)


magic_link_token = MagicLinkTokenGenerator()