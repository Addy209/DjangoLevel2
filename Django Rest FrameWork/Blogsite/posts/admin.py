from django.contrib import admin

# Register your models here.
from  .models import *

admin.site.register(PostDB)
admin.site.register(Comment)