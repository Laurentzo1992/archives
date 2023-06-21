
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('paramettre.urls')),
    path('', include('transfert.urls')),
    path('', include('fond.urls')),
    path('', include('cote.urls')),
    path('', include('gestion.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)