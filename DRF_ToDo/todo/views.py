from djangorestframework_camel_case.parser import CamelCaseJSONParser
# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Projects, Roles, ProjectUsers, Todo
from .serializers import ProjectsSerializer, RolesSerializer
from .serializers import ProjectUsersSerializer, TodoSerializer


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    parser_classes = [CamelCaseJSONParser]
    # Парсер CamelCase подключил, но в api/projects content все равно отображается по-старому. Что не так делаю - ??


class RolesModelViewSet(ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class ProjectUsersModelViewSet(ModelViewSet):
    queryset = ProjectUsers.objects.all()
    serializer_class = ProjectUsersSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
