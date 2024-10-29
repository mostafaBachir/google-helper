from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Personnalisation de l'administration
admin.site.site_header = _("Administration Backend")
admin.site.site_title = _("Administration Backend")
admin.site.index_title = _("Bienvenue dans l'Administration Backend")