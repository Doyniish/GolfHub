from django.contrib import admin

# Register your models here.
from Users.models import Groups, UserData, UserStats, Round, BackNine, FrontNine

admin.site.register(Groups)
admin.site.register(UserData)
admin.site.register(UserStats)
admin.site.register(Round)
admin.site.register(BackNine)
admin.site.register(FrontNine)