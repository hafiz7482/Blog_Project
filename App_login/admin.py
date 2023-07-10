from django.contrib import admin
from .models  import UserProfile, ProfileInfo

# Register your models here.

admin.site.register(UserProfile)

@admin.register(ProfileInfo)
class ProfileInfoModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','mobile','zipcode','state']