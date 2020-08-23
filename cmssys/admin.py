from django.contrib import admin
from .models import CmsUser, AuditLog

# Register your models here.
admin.site.register(AuditLog)
admin.site.register(CmsUser)