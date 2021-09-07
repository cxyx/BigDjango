from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/', include('apps.users.urls')),
    path('rbac/', include(('rbac.urls', 'rbac'), namespace='rbac')),
]
