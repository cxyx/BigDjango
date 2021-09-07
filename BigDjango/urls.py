from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/', include('apps.users.urls')),
    path('rbac/', include(('rbac.urls', 'rbac'), namespace='rbac')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
