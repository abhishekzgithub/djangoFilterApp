from django.urls import path
from .views import home, search
from django_filters.views import FilterView
from .filters import RatingFilter



urlpatterns=[
    path('', home,name='home'),
    path('search/', FilterView.as_view(filterset_class=RatingFilter,
        template_name='search.html'), name='search'),
    
]
