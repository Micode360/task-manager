from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'password', 'role' , 'is_staff', 'is_superuser')
    search_fields = ('first_name', 'email')

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
