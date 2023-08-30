from .models import Book,Reader
import django_filters

class reader_filter(django_filters.filterset):
    year = django_filters.CharFilter(field_name='Borrowed_books__published_year',lookup_expr='gt')
    class meta:
        model = Reader
        fields = []