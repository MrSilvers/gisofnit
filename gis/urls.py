from django.urls import path
from gis import views
app_name = 'gis'

urlpatterns = [
    path('gis/',views.index,name='index'),
]
