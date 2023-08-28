import django_filters
from .models import Blog

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    pub_date = django_filters.NumberFilter(field_name='pub_date', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__last_name', lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ['title', 'pub_date', 'author']
