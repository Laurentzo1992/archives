from django.contrib import admin

from paramettre.models import Archive_statuts, Archive_type, Document_type, Provenance

admin.site.register(Archive_statuts)
admin.site.register(Archive_type)
admin.site.register(Document_type)
admin.site.register(Provenance)