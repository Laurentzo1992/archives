from  django.urls import  path
from  . import views

urlpatterns = [
            path('fond/serie', views.serie, name="serie"),
            path('fond/serie/add', views.add_serie, name="add_serie"),
            path('fond/serie/edit/<int:id>', views.edit_serie, name="edit_serie"),
            path('fond/serie/delete/<int:id>', views.delete_serie, name="delete_serie"),
            
            
            
            path('fond/sousserie', views.sousserie, name="sousserie"),
            path('fond/sousserie/add', views.add_sousserie, name="add_sousserie"),
            path('fond/sousserie/edit/<int:id>', views.edit_sousserie, name="edit_sousserie"),
            path('fond/sousserie/delete/<int:id>', views.delete_sousserie, name="delete_sousserie"),
            
            
            
            path('fond/soussousserie', views.soussousserie, name="soussousserie"),
            path('fond/soussousserie/add', views.add_soussousserie, name="add_soussousserie"),
            path('fond/soussousserie/edit/<int:id>', views.edit_soussousserie, name="edit_soussousserie"),
            path('fond/soussousserie/delete/<int:id>', views.delete_soussousserie, name="delete_soussousserie"),
    
    
]
