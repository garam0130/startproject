from django.conf.urls import url

urlpatterns = [
    url(r'^login/email/$', 'accounts.views.email_login', name='email_login'),
    url(r'^login/email/(?P<token>[0-9a-f]{32})/$', 'accounts.views.email_login_check', name='email_login_check'),
    url(r'^signup/$', 'accounts.views.signup', name='signup'),
]