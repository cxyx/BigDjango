from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
from .resource import UserProfileResource
admin.site.site_header = 'simpleui管理后台'  # 设置header
admin.site.site_title = 'simpleui管理后台'   # 设置title
admin.site.index_title = 'simpleui管理后台'

# Register your models here.
# admin.site.register(models.UserProfile)
# admin.site.register(models.Permission)
# admin.site.register(models.Organization)
# admin.site.register(models.Role)
# admin.site.register(models.Menu)


@admin.register(models.UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    resource_class = UserProfileResource
    list_display = ['id','name','mobile','email','image','department','position']
    search_fields = ['name','mobile','position','superior','roles']
    list_filter = ['name','department']
    list_per_page = 100