from django.contrib import admin
from .models import *

admin.site.register([Member,Tag,Question,Answer,Vote])

# Register your models here.
