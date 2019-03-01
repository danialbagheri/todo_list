from django.contrib import admin

from .models import Designer, Todo, Comment, TodoFile

admin.site.register(Designer)
admin.site.register(Todo)
admin.site.register(Comment)
admin.site.register(TodoFile)
# Register your models here.
