from .views import DetailsView 
from django.urls import include,path
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView


urlpatterns = {
    path('people/', CreateView.as_view(), name="create"),
    path('people/<int:pk>/', DetailsView.as_view(), name="details"),
}
        
urlpatterns = format_suffix_patterns(urlpatterns)

