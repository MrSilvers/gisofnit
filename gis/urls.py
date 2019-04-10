from django.urls import path
from gis import views
app_name = 'gis'

urlpatterns = [
    path('gis/',views.index,name='index'),
    path('gis/addMarker1/',views.add_marker1,name='add_marker1'),
    path('gis/addMarker2/',views.add_marker2,name='add_marker2'),
    path('gis/getMarker/',views.ajax_get_marker_list,name='get_marker'),
    path('gis/add/',views.add_matker_ajax,name='add'),
    path('gis/search/',views.search,name="search"),
    path('gis/ajax/search/',views.ajax_search,name="ajax_search"),
    path('gis/route/',views.route_plan,name="route_plan"),
    path("gis/admin/",views.data_admin,name='data_admin'),
    path("gis/ajax/edit",views.edit,name='edit'),
    path("gis/admin/edit/<int:id>",views.edit_page,name="edit_page"),
    path("gis/admin/delete/<int:id>",views.delete,name="delete"),
    path("gis/admin/search/",views.admin_search,name="admin_search"),
]
