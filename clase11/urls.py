from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Habilita el cambio de idioma
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)
