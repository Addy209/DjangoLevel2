from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Appuser)
admin.site.register(AppUserAddresses)
admin.site.register(state)
admin.site.register(city)
admin.site.register(area)