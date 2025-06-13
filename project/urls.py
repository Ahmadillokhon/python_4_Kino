from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.common.urls')),
    path('movies/', include('apps.movies.urls')),
    path('urls/', include('apps.users.urls')),
    path('', include('apps.users.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
