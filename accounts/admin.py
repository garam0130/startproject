from django.contrib import admin
from accounts.models import EmailToken


class EmailTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'expire_at')

admin.site.register(EmailToken)