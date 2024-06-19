from django.contrib import admin

from api.models import Task, Note


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'created', 'updated', 'deleted', 'is_deleted')
    list_filter = ('status', 'is_deleted')
    ordering = ('created', )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created', 'updated', 'deleted', 'is_deleted')
    list_filter = ('is_deleted', )
    ordering = ('created', )
