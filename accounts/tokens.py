from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.conf import settings

signer = TimestampSigner(salt="email-confirm")


def generate_email_confirm_token(user):
    return signer.sign(user.pk)


def verify_email_confirm_token(token):
    try:
        unsigned = signer.unsign(token, max_age=getattr(settings, 'TOKEN_EXPIRY_SECONDS', 3600))
        return int(unsigned)
    except (BadSignature, SignatureExpired):
        return None


def generate_temporary_password():
    return signer.sign("temporary")

