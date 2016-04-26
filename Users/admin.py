from django.contrib import admin

# Register your models here.
from Users.models import Groups, UserData

admin.site.register(Groups)
admin.site.register(UserData)