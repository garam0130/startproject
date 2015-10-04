from django.contrib import admin
from blog.models import Group, GroupType, SiType, GuType, Apply, Status
# Register your models here.
admin.site.register(Group)
admin.site.register(GroupType)
admin.site.register(SiType)
admin.site.register(GuType)
admin.site.register(Apply)
admin.site.register(Status)