from django.db import models
from django.utils import timezone


class SoftDeleteBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created Date Time')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated Date Time')
    deleted = models.DateTimeField(null=True, blank=True, verbose_name='Deleted Date Time')
    is_deleted = models.BooleanField(default=False, verbose_name='Is Deleted')

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted = timezone.now()
        self.save()


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Task(SoftDeleteBaseModel):
    TODO = 1
    IN_PROGRESS = 2
    DOWN = 3

    STATUS_CHOICES = (
        (TODO, 'todo'),
        (IN_PROGRESS, 'in_progress'),
        (DOWN, 'down'),
    )

    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    status = models.IntegerField(choices=STATUS_CHOICES)

    objects = models.Manager()
    soft_delete_objects = SoftDeleteManager()

    class Meta:
        db_table = 'tasks'
        ordering = ['created']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Note(SoftDeleteBaseModel):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')

    objects = models.Manager()
    soft_delete_objects = SoftDeleteManager()

    class Meta:
        db_table = 'notes'
        ordering = ['created']
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
