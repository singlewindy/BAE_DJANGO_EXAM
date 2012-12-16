from django.contrib import admin
from mysite.users.models import Users, Hackmes

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'psw', 'score', 'update_time')
    search_fields = ('name', )

class HackmesAdmin(admin.ModelAdmin):
	list_display = ('id', 'score', 'title', 'problem', 'tip', 'true','result')

admin.site.register(Users, UsersAdmin)
admin.site.register(Hackmes, HackmesAdmin)