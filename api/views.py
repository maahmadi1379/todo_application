from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from api.models import Task, Note
from api.serializers import TaskSerializer, NoteSerializer
from utils.fulltext_search import simple_fulltext_search
from utils.paginations import StandardResultsSetPagination


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.soft_delete_objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search', openapi.IN_QUERY, description="Search query", type=openapi.TYPE_STRING
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if 'search' in request.query_params:
            search = request.query_params['search']
            queryset = simple_fulltext_search(queryset, search)
        serializer = self.get_serializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.soft_delete_objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search', openapi.IN_QUERY, description="Search query", type=openapi.TYPE_STRING
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if 'search' in request.query_params:
            search = request.query_params['search']
            queryset = simple_fulltext_search(queryset, search)
        serializer = self.get_serializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(serializer.data, status=status.HTTP_200_OK)
