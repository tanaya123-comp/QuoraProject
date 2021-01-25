import django_filters
from .models import *


class TagFilter(django_filters.FilterSet):
    class Meta:
        model=Tag
        fields=('name',)

