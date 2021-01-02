from django.contrib import admin
from .models import *


admin.site.register([Member,Tag,Question,Vote])

# Register your models here.
@admin.register(Answer)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('QuoraApp/js/tinyinject.js')


