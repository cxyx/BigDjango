from import_export import resources
from .models import *


class UserProfileResource(resources.ModelResource):

    class Meta:
        model = UserProfile
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['name','mobile','email','image','department','position','superior','roles']