from django.contrib import admin
from .models import TaskModel

# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'deadline', 'image')
    search_fields = ('name', 'deadline')

admin.site.register(TaskModel, AdminModel)