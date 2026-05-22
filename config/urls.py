from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('projects/', include('apps.projects.urls')),
    path('about/', include('apps.about.urls')),
    path('blog/', include('apps.blog.urls')),
    path('publications/', include('apps.publications.urls')),
    path('contact/', include('apps.contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
