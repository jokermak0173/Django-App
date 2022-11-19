from django.contrib import admin
from .models import  Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'priority')
    search_fields = ('id', 'user', 'title', 'priority')

admin.site.register(Task, TaskAdmin)