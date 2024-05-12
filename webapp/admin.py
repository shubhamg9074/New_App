from django.contrib import admin
from webapp.models import users
# Register your models here.

class Modeladmin(admin.ModelAdmin):
    list_display = ['user_id','name','email','role']
admin.site.register(users,Modeladmin)
