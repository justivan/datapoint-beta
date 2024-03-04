from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include("api.urls", namespace="api")),
    path("grappelli/", include("grappelli.urls")),
    path("accommodation/", include("accommodation.urls", namespace="accommodation")),
    path(settings.ADMIN_URL, admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
