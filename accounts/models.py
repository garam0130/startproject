from uuid import uuid4
from datetime import timedelta
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class EmailToken(models.Model):

    def make_expire_at():
        return timezone.now() + timedelta(hours=1)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    token = models.UUIDField(default=uuid4, editable=False)
    expire_at = models.DateTimeField(default=make_expire_at, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_expired(self):
        return self.expire_at < timezone.now()

    def send_mail(self, request):
        host = request.scheme + '://' + request.get_host()
        url = host + reverse('email_login_check', args=[self.token.hex])

        title = '로그인 링크'
        message = '''
아래 주소를 통해 로그인하실 수 있습니다.

{}'''.format(url)

        send_mail(title, message, settings.EMAIL_HOST_USER, [self.user.email], fail_silently=False)