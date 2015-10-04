from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from accounts.forms import SignupForm, EmailLoginForm
from accounts.models import EmailToken


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, user)

            messages.success(request, '{} 님. 이메일을 확인해주세요.'.format(user))
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/go.html', {
        'form': form,
    })


def email_login(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email_token = form.save()
            email_token.send_mail(request)

            messages.success(request, '{} 이메일로 로그인 링크를 전달했습니다.'.format(email_token.user.email))
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = EmailLoginForm()
    return render(request, 'form.html', {
        'form': form,
    })


def email_login_check(request, token):
    email_token = get_object_or_404(EmailToken, token=token)
    if email_token.is_expired:
        messages.error(request, '만료된 토큰입니다.')
        return redirect('/')
    else:
        user = email_token.user
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)

        messages.success(request, '{} 님. 환영합니다.'.format(user))
        return redirect('/')

