from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('Create_List', views.Create_List, name='Create_List'),
    path('Show_page', views.Show_page, name='Show_page'),
    path('Show_data', views.Show_data, name='Show_data'),
    path('Delete_Data/<int:pk>', views.Delete_Data, name='Delete_Data'),
    path('update_page/<int:pk>', views.update_page, name="update_page"),
    path('update_data/<int:pk>', views.update_data, name='update_data'),
]
