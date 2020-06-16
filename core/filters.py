import django_filters
from .models import Rating

class RatingFilter(django_filters.FilterSet):
    classtype = django_filters.CharFilter(lookup_expr='icontains')
    rate = django_filters.NumberFilter()
    date = django_filters.DateFromToRangeFilter(field_name='date',label='Date (Between) in format YYYY-MM-DD')
    class Meta:
        model = Rating
        fields = "__all__"