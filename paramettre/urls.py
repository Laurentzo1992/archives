from  django.urls import  path
from  . import views

urlpatterns = [
    path('paramettre/status', views.archive_statut, name="archive_statut"),
    path('paramettre/status/add', views.add_statut, name="add_statut"),
    path('paramettre/status/edit/<int:id>', views.edit_statut, name="edit_statut"),
    path('paramettre/status/delete/<int:id>', views.delete_statut, name="delete_statut"),
    
    
    
    path('paramettre/type', views.archive_type, name="archive_type"),
    path('paramettre/type/add', views.add_type, name="add_type"),
    path('paramettre/type/edit/<int:id>', views.edit_type, name="edit_type"),
    path('paramettre/type/delete/<int:id>', views.delete_type, name="delete_type"),
    
    
    path('paramettre/document', views.document_type, name="document_type"),
    path('paramettre/document/add', views.add_document, name="add_document"),
    path('paramettre/document/edit/<int:id>', views.edit_document, name="edit_document"),
    path('paramettre/document/delete/<int:id>', views.delete_document, name="delete_document"),
    
    
    
    path('paramettre/provenance', views.provenance, name="provenance"),
    path('paramettre/provenance/add', views.add_provenance, name="add_provenance"),
    path('paramettre/provenance/edit/<int:id>', views.edit_provenance, name="edit_provenance"),
    path('paramettre/provenance/delete/<int:id>', views.delete_provenance, name="delete_provenance"),
    
    
]
