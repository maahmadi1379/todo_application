from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    TaskViewSet,
    NoteViewSet,
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
