from  django.urls import  path
from  . import views

urlpatterns = [
            path('cote/site', views.site, name="site"),
            path('cote/site/add', views.add_site, name="add_site"),
            path('cote/site/edit/<int:id>', views.edit_site, name="edit_site"),
            path('cote/site/delete/<int:id>', views.delete_site, name="delete_site"),
            
            
            
            path('cote/salle', views.salle, name="salle"),
            path('cote/salle/add', views.add_salle, name="add_salle"),
            path('cote/salle/edit/<int:id>', views.edit_salle, name="edit_salle"),
            path('cote/salle/delete/<int:id>', views.delete_salle, name="delete_salle"),
            
            
            
            path('cote/travee', views.travee, name="travee"),
            path('cote/travee/add', views.add_travee, name="add_travee"),
            path('cote/travee/edit/<int:id>', views.edit_travee, name="edit_travee"),
            path('cote/travee/delete/<int:id>', views.delete_travee, name="delete_travee"),
            
            
            
            path('cote/rayon', views.rayon, name="rayon"),
            path('cote/rayon/add', views.add_rayon, name="add_rayon"),
            path('cote/rayon/edit/<int:id>', views.edit_rayon, name="edit_rayon"),
            path('cote/rayon/delete/<int:id>', views.delete_rayon, name="delete_rayon"),
            
            
            path('cote/boite', views.boite, name="boite"),
            path('cote/boite/add', views.add_boite, name="add_boite"),
            path('cote/boite/edit/<int:id>', views.edit_boite, name="edit_boite"),
            path('cote/boite/delete/<int:id>', views.delete_boite, name="delete_boite"),
    
            ]
