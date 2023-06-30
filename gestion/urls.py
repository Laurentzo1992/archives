from  django.urls import  path
from  . import views

urlpatterns = [
 
            path('gestion/archive', views.archive, name='archive'),
            path('gestion/archive/add', views.add_archive, name='add_archive'),
            path('gestion/archive/edit', views.edit_archive, name='edit_archive'),
            path('gestion/archive/delete', views.delete_archive, name='delete_archive'),
            
            
            
            
            path('gestion/archive/search', views.search, name='search'),
]
