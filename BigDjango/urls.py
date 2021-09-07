from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/', include('apps.users.urls')),
    path('rbac/', include(('rbac.urls', 'rbac'), namespace='rbac')),
    path('app01/', include(('app01.urls', 'app01'), namespace='app01')),
    path('v1/', include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
