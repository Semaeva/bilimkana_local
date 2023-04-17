
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as yasgurls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('server.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *yasgurls
]
