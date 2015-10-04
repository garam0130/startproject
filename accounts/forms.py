from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import EmailToken


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('이미 등록된 이메일주소가 아닙니다.')
        return email

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EmailLoginForm(forms.Form):
    email = forms.EmailField(help_text='가입하셨던 이메일 주소를 입력해주세요.')

    def clean_email(self):
        email = self.cleaned_data.get('email', '')

        if email:
            User = get_user_model()

            try:
                self.user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError('등록된 이메일주소가 아닙니다.')

            if not self.user.is_active:
                raise forms.ValidationError('비활성화된 계정입니다. 관리자에게 문의해주세요.')

        return email

    def save(self, commit=True):
        email_token = EmailToken(user=self.user)
        if commit:
            email_token.save()
        return email_token

